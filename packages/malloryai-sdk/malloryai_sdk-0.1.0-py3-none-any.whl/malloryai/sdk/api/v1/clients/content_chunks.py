from typing import List, Dict, Any, Optional

from malloryai.sdk.api.v1.http_client import HttpClient


class ContentChunksClient:
    """Client for managing content chunks."""

    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    async def list_content_chunks(
        self, filter_by: Optional[str] = "", offset: int = 0, limit: int = 100
    ) -> List[Dict[str, Any]]:
        """
        List content chunks.
        :param filter_by: Filter content chunks by available filters.
        :param offset: Offset for pagination.
        :param limit: Limit for pagination.
        :return: List of content chunks.
        """
        params = {"filter": filter_by, "offset": offset, "limit": limit}
        return await self.http_client.get("/content_chunks", params=params)

    async def get_content_chunk(self, identifier: str) -> Dict[str, Any]:
        return await self.http_client.get(f"/content_chunks/{identifier}")
