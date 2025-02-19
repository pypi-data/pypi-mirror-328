from typing import List, Dict, Any, Optional

from malloryai.sdk.api.v1.decorators.sorting import validate_sorting
from malloryai.sdk.api.v1.http_client import HttpClient


class ThreatActorsClient:
    """Client for managing threat actors."""

    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    async def list_threat_actors(
        self, filter: Optional[str] = "", offset: int = 0, limit: int = 100
    ) -> List[Dict[str, Any]]:
        """
        List threat actors.
        :param filter:
        :param offset: Offset for pagination.
        :param limit: Limit for pagination.
        :return: List of threat actors.
        """
        params = {"filter": filter, "offset": offset, "limit": limit}
        return await self.http_client.get("/actors", params=params)

    async def get_threat_actor(self, identifier: str) -> Dict[str, Any]:
        """
        Get a threat actor by identifier.
        :param identifier: The unique UUID or name of the threat actor to retrieve.
        :return: Threat actor.
        """
        return await self.http_client.get(f"/actors/{identifier}")

    @validate_sorting(
        sort_pattern="^(created_at|updated_at|published_at|collected_at)$"
    )
    async def list_threat_actors_mentioned(
        self,
        offset: int = 0,
        limit: int = 100,
        sort: str = "created_at",
        order: str = "desc",
    ) -> List[Dict[str, Any]]:
        """
          List threat actors mentioned.
        :param offset: Offset for pagination.
        :param limit: Limit for pagination.
        :param sort: Sorting field.
        :param order: Sorting order.
        :return: List of threat actors mentioned.
        """
        params = {"offset": offset, "limit": limit, "sort": sort, "order": order}
        return await self.http_client.get("/mentions/actors", params=params)
