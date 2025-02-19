from typing import List, Dict, Any

from malloryai.sdk.api.v1.http_client import HttpClient


class SourcesClient:
    """Client for managing sources."""

    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    async def list_sources(self) -> List[Dict[str, Any]]:
        """
        List all sources.
        :return: List of sources.
        """
        return await self.http_client.get("/sources")
