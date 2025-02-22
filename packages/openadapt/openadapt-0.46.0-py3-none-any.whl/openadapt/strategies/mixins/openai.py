"""Implements a ReplayStrategy mixin for generating LLM completions.

Usage:

    class MyReplayStrategy(OpenAIReplayStrategyMixin):
        ...
"""

from pprint import pformat
import time

import openai
import tiktoken

from openadapt import cache, models
from openadapt.config import config
from openadapt.custom_logger import logger
from openadapt.strategies.base import BaseReplayStrategy

# https://github.com/nalgeon/pokitoki/blob/0b6b921d367f693738e7b9bab44e6926171b48d6/bot/ai/chatgpt.py#L78
# OpenAI counts length in tokens, not characters.
# We also leave some tokens reserved for the output.
MAX_LENGTHS = {
    # max 4096 tokens total, max 3072 for the input
    "gpt-3.5-turbo": int(3 * 1024),
    # max 8192 tokens total, max 7168 for the input
    "gpt-4": int(7 * 1024),
    "gpt-4-32k": 32768,
}
MODEL_NAME = "gpt-4"

openai.api_key = config.OPENAI_API_KEY
encoding = tiktoken.get_encoding("cl100k_base")


class OpenAIReplayStrategyMixin(BaseReplayStrategy):
    """Mixin class implementing replay strategy using OpenAI models."""

    def __init__(
        self,
        recording: models.Recording,
        model_name: str = config.OPENAI_MODEL_NAME,
        # system_message: str = config.OPENAI_SYSTEM_MESSAGE,
    ) -> None:
        """Initialize the OpenAIReplayStrategyMixin.

        Args:
            recording (models.Recording): The recording object.
            model_name (str): The name of the OpenAI model to use.

        """
        super().__init__(recording)

        logger.info(f"{model_name=}")
        self.model_name = model_name
        # self.system_message = system_message

    def get_completion(
        self,
        prompt: str,
        system_message: str,
        # max_tokens: int,
    ) -> str:
        """Generates an LLM completion.

        Args:
            prompt (str): The prompt for the completion.
            system_message (str): The system message to set the context.

        Returns:
            str: The generated completion.
        """
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt},
        ]
        logger.debug(f"messages=\n{pformat(messages)}")
        completion = create_openai_completion(self.model_name, messages)
        logger.debug(f"completion=\n{pformat(completion)}")
        choices = completion["choices"]
        choice = choices[0]
        message = choice["message"]
        content = message["content"]
        return content


@cache.cache()
def create_openai_completion(
    model: str,
    messages: list,
    # temperatere=1,
    # top_p=1,
    # n=1,
    # stream=False,
    # stop=None,
    # max_tokens=inf,
    # presence_penalty=0,
    # frequency_penalty=0,
    # logit_bias=None,
    # user=None,
) -> dict:
    """Creates an LLM completion using the OpenAI API.

    Args:
        model (str): The model name.
        messages (list): The list of messages.

    Returns:
        dict: The completion response.
    """
    return openai.ChatCompletion.create(
        model=model,
        messages=messages,
        # temperatere=temperature,
        # top_p=top_p,
        # n=n,
        # stream=stream,
        # stop=stop,
        # max_tokens=max_tokens,
        # presence_penalty=presence_penalty,
        # frequency_penalty=frequency_penalty,
        # logit_bias=logit_bias,
        # user=user,
    )


@cache.cache()
def get_completion(
    messages: list,
    prompt: str,
    model: str = "gpt-4",
) -> list[str]:
    """Gets the LLM completion.

    Args:
        messages (list): The list of messages.
        prompt (str): The prompt for the completion.
        model (str): The model name.

    Returns:
        list: The list of messages with the generated completion.
    """
    logger.info(f"{prompt=}")

    messages.append({"role": "user", "content": prompt})
    # length = MAX_LENGTHS[model]
    # shorten_messages(messages, length)
    logger.debug(f"messages=\n{pformat(messages)}")

    def _get_completion(prompt: str) -> str:
        """Helper function to get the LLM completion.

        Args:
            prompt (str): The prompt for the completion.

        Returns:
            str: The generated completion.
        """
        try:
            completion = create_openai_completion(model, messages)
            logger.info(f"{completion=}")
        except openai.error.InvalidRequestError as exc:
            logger.exception(f"{exc=}")
            completion = ""

        return completion

    sleep_time = 10
    while True:
        try:
            completion = _get_completion(prompt)
        except openai.error.RateLimitError as exc:
            logger.exception(f"{exc=}")
            logger.warning(f"{sleep_time=}")
            time.sleep(sleep_time)
            sleep_time *= 2
        else:
            break
    choices = completion["choices"]
    choice = choices[0]
    message = choice["message"]
    content = message["content"]

    assistant_message = {
        "role": "assistant",
        "content": content,
    }
    logger.debug(f"appending assistant_message=\n{pformat(assistant_message)}")
    messages.append(assistant_message)
    return messages
