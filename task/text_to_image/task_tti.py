import asyncio
from datetime import datetime

from task._models.custom_content import Attachment
from task._utils.constants import API_KEY, DIAL_URL, DIAL_CHAT_COMPLETIONS_ENDPOINT
from task._utils.bucket_client import DialBucketClient
from task._utils.model_client import DialModelClient
from task._models.message import Message
from task._models.role import Role


async def _save_images(attachments: list[Attachment]):
    """Async function to download and save images"""

    async with DialBucketClient(
            api_key=API_KEY,
            base_url=DIAL_URL
    ) as bucket_client:
        for attachment in attachments:
            if attachment.type and attachment.type == 'image/png':
                image_data = await bucket_client.get_file(attachment.url)
                filename = f"{datetime.now()}.png"

                with open(filename, 'wb') as f:
                    f.write(image_data)

                print(f"Image saved: {filename}")


def start() -> None:
    dalle_client = DialModelClient(
        endpoint=DIAL_CHAT_COMPLETIONS_ENDPOINT,
        deployment_name='dall-e-3',
        api_key=API_KEY,
    )

    user_input = 'Sunny day on Bali'

    ai_message = dalle_client.get_completion(
        [Message(role=Role.USER, content=user_input)]
    )

    if custom_content := ai_message.custom_content:
        if attachments := custom_content.attachments:
            asyncio.run(_save_images(attachments))


start()
