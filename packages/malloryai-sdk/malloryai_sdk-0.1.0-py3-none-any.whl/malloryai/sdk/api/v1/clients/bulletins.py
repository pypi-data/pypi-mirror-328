from typing import List, Dict, Any

from malloryai.sdk.api.v1.http_client import HttpClient


class BulletinsClient:
    """Client for managing bulletins."""

    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    async def list_bulletins(
        self,
        offset: int = 0,
        limit: int = 100,
    ) -> List[Dict[str, Any]]:
        """
        List all bulletins.
        :param offset: Offset for pagination
        :param limit: Limit for pagination
        :return: List of bulletins
        """
        params = {"offset": offset, "limit": limit}
        return await self.http_client.get("/bulletins", params=params)

    async def get_bulletin(self, identifier: str) -> Dict[str, Any]:
        """
        Get a bulletin by identifier.
        :param identifier: Identifier of the bulletin
        :return: Bulletin
        """
        return await self.http_client.get(f"/bulletins/{identifier}")
