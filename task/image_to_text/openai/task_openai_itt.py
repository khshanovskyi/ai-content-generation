import base64
from pathlib import Path

from task._utils.constants import API_KEY, DIAL_CHAT_COMPLETIONS_ENDPOINT
from task._utils.model_client import DialModelClient
from task._models.role import Role
from task.image_to_text.openai.message import ContentedMessage, TxtContent, ImgContent, ImgUrl

# ------------------------
# THIS TASK IS OPTIONAL
# ------------------------

def start() -> None:
    project_root = Path(__file__).parent.parent.parent.parent
    image_path = project_root / "dialx-banner.png"

    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
    base64_image = base64.b64encode(image_bytes).decode('utf-8')

    dalle_client = DialModelClient(
        endpoint=DIAL_CHAT_COMPLETIONS_ENDPOINT,
        deployment_name='gpt-4o',
        api_key=API_KEY,
    )

    dalle_client.get_completion(
        [
            ContentedMessage(
                role=Role.USER,
                content=[
                    TxtContent(
                        text="What do you see on this picture?"
                    ),
                    ImgContent(
                        image_url=ImgUrl(
                            url=f"data:image/png;base64,{base64_image}"
                        )
                    )
                ]
            )
        ]
    )


start()