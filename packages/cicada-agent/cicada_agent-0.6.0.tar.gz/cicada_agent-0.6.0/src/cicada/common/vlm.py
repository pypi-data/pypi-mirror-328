import logging
from abc import ABC
from typing import List, Union

import httpx
import openai
import tenacity

from cicada.common import llm
from cicada.common.utils import colorstring, cprint

logger = logging.getLogger(__name__)


class VisionLanguageModel(llm.LanguageModel, ABC):
    def __init__(
        self,
        api_key: str,
        api_base_url: str,
        model_name: str,
        org_id: str,
        **model_kwargs,
    ):
        """
        Initialize the VisionLanguageModel.

        :param api_key: The API key for the OpenAI service.
        :param api_base_url: The base URL for the OpenAI API.
        :param model_name: The name of the model to use.
        :param org_id: The organization ID for the OpenAI service.
        :param model_kwargs: Additional keyword arguments for the model.
        """
        super().__init__(
            api_key,
            api_base_url,
            model_name,
            org_id,
            **model_kwargs,
        )

    def _prepare_prompt(
        self,
        images_with_text: List[Union[str, bytes]] | None = None,
        prompt: str | None = None,
        images: bytes | List[bytes] | None = None,
        max_items_per_message: int = 4,  # Adjust as needed
    ) -> List[dict]:
        """
        Prepare the prompt for the API by splitting the content into multiple messages if needed.

        :param images_with_text: A list of mixed text (str) and image (bytes) data.
        :param prompt: Optional user prompt text.
        :param images: Optional image data (single or list of bytes).
        :param max_items_per_message: Maximum items per message.
        :return: A list of messages with prepared content.
        """
        content = []
        messages = []

        if prompt:
            messages.append({"role": "user", "content": prompt})

        # either images or images_with_text
        # Handle images
        if images:
            if not isinstance(images, list):
                images = [images]
            content = []
            for image_data in images:
                content.append(
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},
                    }
                )
                if len(content) >= max_items_per_message:
                    messages.append({"role": "user", "content": content})
                    content = []
            if content:  # Add remaining items
                messages.append({"role": "user", "content": content})

        # Handle images_with_text
        elif images_with_text:
            content = []
            for item in images_with_text:
                if isinstance(item, str):
                    content.append({"type": "text", "text": item})
                elif isinstance(item, bytes):
                    content.append(
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{item}"},
                        }
                    )
                else:
                    raise ValueError(
                        f"Unsupported type in images_with_text: {type(item)}"
                    )
                if len(content) >= max_items_per_message:
                    messages.append({"role": "user", "content": content})
                    content = []
            if content:  # Add remaining items
                messages.append({"role": "user", "content": content})

        return messages

    @tenacity.retry(
        stop=tenacity.stop_after_attempt(3)
        | tenacity.stop_after_delay(30),  # Stop after 3 attempts or 30 seconds
        wait=tenacity.wait_random_exponential(multiplier=1, min=2, max=10),
        retry=tenacity.retry_if_exception_type(
            (openai.APIError, httpx.ReadTimeout, httpx.ConnectTimeout)
        ),  # Retry on API errors or network timeouts
        before_sleep=tenacity.before_sleep_log(
            logger, logging.WARNING
        ),  # Log before retrying
        reraise=True,
    )
    def query_with_image(
        self,
        prompt: str | None = None,
        images: bytes | List[bytes] | None = None,
        images_with_text: List[Union[str, bytes]] | None = None,
        system_prompt: str | None = None,
    ) -> str:
        """
        Query the VisionLanguageModel with mixed text and image data.

        :param prompt: Optional user prompt text.
        :param images: Optional image data (single or list of bytes).
        :param images_with_text: Optional list of mixed text (str) and image (bytes) data.
        :param system_prompt: Optional system prompt text.
        :return: Generated response from the model.
        """
        full_prompt = self._prepare_prompt(
            images_with_text=images_with_text, prompt=prompt, images=images
        )
        logger.info(colorstring(len(full_prompt), "white"))
        if system_prompt:
            full_prompt = [
                {"role": "system", "content": system_prompt},
            ] + full_prompt

        # Use stream from configuration
        stream = self.stream

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=full_prompt,
            stream=stream,
            **self.model_kwargs,
        )

        if stream:
            complete_response = ""
            for chunk in response:
                chunk_content = chunk.choices[0].delta.content
                if chunk_content:
                    cprint(chunk_content, "white", end="", flush=True)
                    complete_response += chunk_content
            print()  # Add a newline after the response
            return complete_response.strip()
        else:
            return response.choices[0].message.content.strip()


# Example usage
if __name__ == "__main__":
    import argparse

    from cicada.common.utils import image_to_base64, load_config, setup_logging

    parser = argparse.ArgumentParser(description="Vision Language Model")
    parser.add_argument(
        "--config", default="config.yaml", help="Path to the configuration YAML file"
    )
    parser.add_argument("--image", required=True, help="Path to the testing image")
    args = parser.parse_args()
    setup_logging()

    vlm_config = load_config(args.config, "vlm")

    image_path = args.image
    image_data = image_to_base64(image_path)

    vlm = VisionLanguageModel(
        vlm_config["api_key"],
        vlm_config.get("api_base_url"),
        vlm_config.get("model_name", "gpt-4o"),
        vlm_config.get("org_id"),
        **vlm_config.get("model_kwargs", {}),
    )
    response = vlm.query_with_image(
        "Describe this image.",
        image_data,
        system_prompt="you are great visual describer.",
    )
    if not vlm.stream:
        logger.info(colorstring(response, "white"))
    response = vlm.query("who made you?")
    if not vlm.stream:
        logger.info(colorstring(response, "white"))
