import json
from typing import Any

import requests

from task._models.message import Message
from task._utils.request import print_request


class DialModelClient:
    _endpoint: str
    _api_key: str

    def __init__(self, endpoint: str, deployment_name: str, api_key: str):
        if not api_key or api_key.strip() == "":
            raise ValueError("API key cannot be null or empty")

        self._endpoint = endpoint.format(
            model=deployment_name
        )
        self._api_key = api_key


    def get_completion(self, messages: list[Message], custom_fields: dict[str, Any] | None = None, **kwargs) -> Message:
        headers = {
            "api-key": self._api_key,
            "Content-Type": "application/json"
        }

        request_data: dict[str, Any] = {
            "messages": [msg.to_dict() for msg in messages],
            **kwargs
        }
        if custom_fields:
            request_data["custom_fields"] = {
                "configuration": {**custom_fields}
            }

        print_request(endpoint=self._endpoint, request_data=request_data, headers=headers)

        response = requests.post(url=self._endpoint, headers=headers, json=request_data)

        if response.status_code == 200:
            data = response.json()
            print(json.dumps(data, indent=2))
            choices = data.get("choices", [])
            if choices:
                if message := choices[0].get("message"):
                    return Message.from_dict(message)
                raise ValueError("No Message has been present in the response")
            raise ValueError("No Choice has been present in the response")
        else:
            raise Exception(f"HTTP {response.status_code}: {response.text}")
