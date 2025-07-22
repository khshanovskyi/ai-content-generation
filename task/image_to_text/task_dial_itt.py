import asyncio
from io import BytesIO
from pathlib import Path

from task._models.custom_content import Attachment, CustomContent
from task._utils.constants import API_KEY, DIAL_URL, DIAL_CHAT_COMPLETIONS_ENDPOINT
from task._utils.bucket_client import DialBucketClient
from task._utils.model_client import DialModelClient
from task._models.message import Message
from task._models.role import Role


async def _put_image() -> Attachment:
    file_name = 'dialx-banner.png'
    image_path = Path(__file__).parent.parent.parent / file_name
    mime_type_png = 'image/png'

    # TODO:
    #  1. Create async context manager: async with DialBucketClient(api_key=API_KEY, base_url=DIAL_URL) as bucket_client:
    #  2. Inside context manager:
    #    - Open image file: with open(image_path, "rb") as f:
    #    - Read file content: image_bytes = f.read()
    #  3. Create BytesIO object: image_content = BytesIO(image_bytes)
    #  4. Upload file: attachment = await bucket_client.put_file(name=file_name, mime_type=mime_type_png, content=image_content)
    #  5. Return Attachment object:
    #    - title=file_name
    #    - url=attachment.get("url")
    #    - type=mime_type_png


def start() -> None:
    # TODO:
    #  1. Create DialModelClient instance:
    #    - endpoint: DIAL_CHAT_COMPLETIONS_ENDPOINT
    #    - deployment_name: 'anthropic.claude-v3-haiku'
    #    - api_key: API_KEY
    #    - Store in variable: dalle_client
    #  2. Upload image: attachment = asyncio.run(_put_image()) - the picture `dialx-banner.png` will be loaded to
    #     DIAL Bucket and we will get Attachment object with URL where file is persists
    #  3. Print attachment to see result: print(attachment)
    #  4. Call dalle_client.get_completion() with list containing one Message:
    #    - role: Role.USER
    #    - content: "What do you see on this picture?"
    #    - custom_content: CustomContent(attachments=[attachment])
    #  ---------------------------------------------------------------------------------------------------------------
    #  Note: This approach uploads the image to DIAL bucket and references it via attachment. The key benefit of this
    #        approach that we can use Models from different vendors (OpenAI, Google, Anthropic). The DIAL Core
    #        adapts this attachment to Message content in appropriate format for Model.
    #  TRY THIS APPROACH WITH DIFFERENT MODELS!
    #  Optional: Try upload 2+ pictures for analysis
    pass


start()
