from http import HTTPStatus
from logging import Logger
import time
from typing import AsyncGenerator, AsyncIterator, Dict, List, Tuple, Union

from furiosa_llm.api import LLM, RequestOutput, SamplingParams
from furiosa_llm.llm_engine import AsyncLLMEngine, TokensPrompt
from furiosa_llm.outputs import RequestOutputKind
from furiosa_llm.server.parse import parse_and_batch_prompt  # type: ignore
from furiosa_llm.server.protocol import (
    CompletionRequest,
    CompletionResponse,
    CompletionResponseChoice,
    CompletionResponseStreamChoice,
    CompletionStreamResponse,
    ErrorResponse,
    UsageInfo,
)
from furiosa_llm.server.serving_base import OpenAIServing
from furiosa_llm.server.utils import AnyTokenizer, merge_async_iterators, random_uuid

logger = Logger(__name__)


class OpenAIServingCompletion(OpenAIServing):
    def __init__(
        self,
        llm: LLM,
    ):
        self.async_llm_engine: AsyncLLMEngine = AsyncLLMEngine.from_llm(llm)
        self.tokenizer: AnyTokenizer = llm.tokenizer
        self.model_name = llm.model_metadata.pretrained_id

    async def create_completion(
        self,
        request: CompletionRequest,
    ) -> Union[AsyncGenerator[str, None], CompletionResponse, ErrorResponse]:
        """Completion API similar to OpenAI's API.

        See https://platform.openai.com/docs/api-reference/completions/create
        for the API specification. This API mimics the OpenAI Completion API.

        NOTE: Currently we do not support the following feature:
            - suffix (the language models we currently support do not support
            suffix)
        """
        request_id = f"cmpl-{random_uuid()}"
        created_time = int(time.time())

        try:
            assert request.max_tokens is not None
            sampling_params = request.to_sampling_params()
        except ValueError as e:
            return self.create_error_response(str(e))

        stream = (
            request.stream
            and (request.best_of is None or request.n == request.best_of)
            and not request.use_beam_search
        )

        parsed_prompts = parse_and_batch_prompt(request.prompt)
        tokens_prompts: List[TokensPrompt] = []
        # When we pass text as an input to AsyncLLMEngine, it encodes it with fixed `add_special_tokens=False`.
        # This is because the chat API, which handles the majority of use cases, passes text with the bos token already prepended due to chat templates.
        # So we need to encode the prompt text here with `add_special_tokens=True` before passing it to the AsyncLLMEngine.
        try:
            for prompt in parsed_prompts:
                if prompt['is_tokens']:
                    tokens_prompts.append(TokensPrompt(prompt_token_ids=prompt['content']))
                else:
                    encoded = self.tokenizer.encode(
                        prompt['content'], padding=False, add_special_tokens=True
                    )
                    tokens_prompts.append(TokensPrompt(prompt_token_ids=encoded))

            sampling_params.output_kind = (
                RequestOutputKind.DELTA if stream else RequestOutputKind.FINAL
            )
            result_generator: List[AsyncGenerator[RequestOutput, None]] = [
                self.async_llm_engine.generate(prompt, sampling_params, request_id)
                for prompt in tokens_prompts
            ]
            merged_generator = merge_async_iterators(*result_generator)
        except ValueError as e:
            return self.create_error_response(str(e))
        except Exception as e:
            logger.error("Error in chat completion: %s", e, exc_info=True)
            return self.create_error_response("internal server error")

        if stream:
            return self.completion_stream_generator(
                merged_generator,
                request_id,
                created_time,
                sampling_params,
            )

        try:
            response = await self.completion_full_generator(
                merged_generator,
                request_id,
                created_time,
            )
            return response
        except ValueError as e:
            return self.create_error_response(str(e))

    async def completion_stream_generator(
        self,
        result_generator: AsyncIterator[Tuple[int, RequestOutput]],
        request_id: str,
        created_time: int,
        sampling_params: SamplingParams,
    ) -> AsyncGenerator[str, None]:
        try:
            async for prompt_idx, output in result_generator:
                chunk = CompletionStreamResponse(
                    id=request_id,
                    created=created_time,
                    model=self.model_name,
                    choices=[
                        CompletionResponseStreamChoice(
                            index=prompt_idx * sampling_params.n + o.index,
                            text=o.text,
                            finish_reason=o.finish_reason,
                            logprobs=None,  # TODO: support logprobs
                        )
                        for o in output.outputs
                    ],
                )
                response_json = chunk.model_dump_json(exclude_unset=False)
                yield f"data: {response_json}\n\n"

            # TODO: support echo
            # TODO: support request.stream_options.include_usage

        except ValueError as e:
            data = self.create_streaming_error_response(str(e))
            yield f"data: {data}\n\n"
        except Exception as e:
            logger.error("Error in chat completion stream: %s", e, exc_info=True)
            data = self.create_streaming_error_response(
                "internal server error",
                err_type="InternalServerError",
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            )
            yield f"data: {data}\n\n"
        yield "data: [DONE]\n\n"

    async def completion_full_generator(
        self,
        result_generator: AsyncIterator[Tuple[int, RequestOutput]],
        request_id: str,
        created_time: int,
    ) -> CompletionResponse:
        last_outputs_only: Dict[int, RequestOutput] = {}
        async for prompt_idx, output in result_generator:
            last_outputs_only[prompt_idx] = output

        request_outputs = [last_outputs_only[i] for i in sorted(last_outputs_only.keys())]
        return self.request_outputs_to_completion_response(
            request_outputs, request_id, created_time
        )

    def request_outputs_to_completion_response(
        self,
        request_outputs: List[RequestOutput],
        request_id: str,
        created_time: int,
    ) -> CompletionResponse:
        choices: List[CompletionResponseChoice] = []
        num_prompt_tokens = 0
        num_generated_tokens = 0

        for request_output in request_outputs:
            prompt_token_ids = request_output.prompt_token_ids

            for output in request_output.outputs:
                # TODO: support echo
                output_text = output.text
                choice_data = CompletionResponseChoice(
                    index=len(choices),
                    text=output_text,
                    finish_reason=output.finish_reason,
                )
                choices.append(choice_data)

            num_prompt_tokens += len(prompt_token_ids)
            num_generated_tokens += sum(len(output.token_ids) for output in request_output.outputs)

        usage = UsageInfo(
            prompt_tokens=num_prompt_tokens,
            completion_tokens=num_generated_tokens,
            total_tokens=num_prompt_tokens + num_generated_tokens,
        )

        return CompletionResponse(
            id=request_id,
            created=created_time,
            model=self.model_name,
            choices=choices,
            usage=usage,
        )
