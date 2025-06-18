from io import BytesIO
from typing import Any, Dict

import httpx


class DialBucketClient:
    def __init__(self, api_key: str , base_url: str):
        self.api_key = api_key
        self.base_url = base_url
        self._bucket_id: str | None = None
        self._client: httpx.AsyncClient | None = None

    async def __aenter__(self):
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={'Api-Key': self.api_key},
        )
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        if self._client:
            await self._client.aclose()


    async def _get_bucket(self) -> str:
        if not self._bucket_id:
            response = await self._client.get('/v1/bucket')
            response.raise_for_status()

            bucket_json = response.json()
            if "appdata" in bucket_json:
                self._bucket_id = bucket_json["appdata"]
            elif "bucket" in bucket_json:
                self._bucket_id = bucket_json["bucket"]
            else:
                raise ValueError("No appdata or bucket found")

        return self._bucket_id


    async def put_file(
        self, name: str, mime_type: str, content: BytesIO
    ) -> Dict[str, Any]:
        path = await self._get_bucket()

        response = await self._client.put(
            f"/v1/files/{path}/{name}",
            files={name: (name, content, mime_type)},
        )
        response.raise_for_status()
        return response.json()

    async def get_file(self, url: str) -> bytes:
        response = await self._client.get(f"/v1/{url}")
        response.raise_for_status()
        return response.content

