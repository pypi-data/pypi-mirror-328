from typing import List, Dict, Any, Optional

from malloryai.sdk.api.v1.decorators.sorting import validate_sorting
from malloryai.sdk.api.v1.http_client import HttpClient


class VulnerabilitiesClient:
    """Client for managing vulnerabilities."""

    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    async def list_vulnerabilities(
        self,
        filter: Optional[str] = "",
        offset: int = 0,
        limit: int = 100,
        sort: str = "created_at",
        order: str = "desc",
    ) -> List[Dict[str, Any]]:
        """
        List vulnerabilities
        :param filter: Filter query.
        :param offset: Offset for pagination.
        :param limit: Limit for pagination.
        :param sort: Sorting field.
        :param order: Sorting order.
        :return:
        """
        params = {
            "filter": filter,
            "offset": offset,
            "limit": limit,
            "sort": sort,
            "order": order,
        }
        return await self.http_client.get("/vulnerabilities", params=params)

    async def get_vulnerability(self, identifier: str) -> Dict[str, Any]:
        """
        Get vulnerability by identifier
        :param identifier: Vulnerability identifier. (CVE, UUID)
        :return: Vulnerability details
        """
        return await self.http_client.get(f"/vulnerabilities/{identifier}")

    async def get_vulnerability_configurations(self, identifier: str) -> Dict[str, Any]:
        """
        Get vulnerability configurations
        :param identifier: Vulnerability identifier. (CVE, UUID)
        :return: Vulnerability configurations
        """
        return await self.http_client.get(
            f"/vulnerabilities/{identifier}/configurations"
        )

    async def get_vulnerability_detection_signatures(
        self, identifier: str
    ) -> Dict[str, Any]:
        """
        Get vulnerability detection signatures
        :param identifier: Vulnerability identifier. (CVE, UUID)
        :return: Vulnerability detection signatures
        """
        return await self.http_client.get(
            f"/vulnerabilities/{identifier}/detection_signatures"
        )

    async def get_vulnerability_exploitations(self, identifier: str) -> Dict[str, Any]:
        """
        Get vulnerability exploitations
        :param identifier: Vulnerability identifier. (CVE, UUID)
        :return: Vulnerability exploitations
        """
        return await self.http_client.get(
            f"/vulnerabilities/{identifier}/exploitations"
        )

    async def get_vulnerability_exploits(self, identifier: str) -> Dict[str, Any]:
        """
        Get vulnerability exploits
        :param identifier: Vulnerability identifier. (CVE, UUID)
        :return: Vulnerability exploits
        """
        return await self.http_client.get(f"/vulnerabilities/{identifier}/exploits")

    async def get_vulnerability_mentions(self, identifier: str) -> Dict[str, Any]:
        """
        Get vulnerability mentions
        :param identifier: Vulnerability identifier. (CVE, UUID)
        :return: Vulnerability mentions
        """
        return await self.http_client.get(f"/vulnerabilities/{identifier}/mentions")

    @validate_sorting
    async def list_vulnerable_configurations(
        self,
        offset: int = 0,
        limit: int = 100,
        sort: str = "created_at",
        order: str = "desc",
    ) -> List[Dict[str, Any]]:
        """
        List vulnerable configurations
        :param offset: Offset for pagination.
        :param limit: Limit for pagination.
        :param sort: Sorting field.
        :param order: Sorting order.
        :return: List of vulnerable configurations
        """
        params = {"offset": offset, "limit": limit, "sort": sort, "order": order}
        return await self.http_client.get("/vulnerable_configurations", params=params)

    async def get_vulnerable_configuration(self, identifier: str) -> Dict[str, Any]:
        """
        Get vulnerable configuration by identifier
        :param identifier: Vulnerable configuration identifier. (UUID)
        :return: Vulnerable configuration details
        """
        return await self.http_client.get(f"/vulnerable_configurations/{identifier}")

    @validate_sorting(
        sort_pattern="^(created_at|updated_at|published_at|collected_at)$"
    )
    async def search_vulnerable_configurations(
        self,
        vendor: str,
        product: str,
        offset: int = 0,
        limit: int = 100,
        sort: str = "created_at",
        order: str = "desc",
    ) -> List[Dict[str, Any]]:
        """
        Search vulnerable configurations
        :param vendor: Vendor name
        :param product: Product name
        :param offset: Offset for pagination.
        :param limit: Limit for pagination.
        :param sort: Sorting field.
        :param order: Sorting order.
        :return: List of vulnerable configurations
        """
        payload = {"vendor": vendor, "product": product}
        params = {"offset": offset, "limit": limit, "sort": sort, "order": order}
        return await self.http_client.post(
            "/vulnerable_configurations/search", json=payload, params=params
        )

    @validate_sorting(
        sort_pattern="^(created_at|updated_at|published_at|collected_at)$"
    )
    async def list_vulnerabilities_mentions(
        self,
        offset: int = 0,
        limit: int = 100,
        sort: str = "created_at",
        order: str = "desc",
    ) -> List[Dict[str, Any]]:
        """
        List vulnerabilities mentions
        :param offset: Offset for pagination.
        :param limit: Limit for pagination.
        :param sort: Sorting field.
        :param order: Sorting order.
        :return: List of vulnerabilities mentions
        """
        params = {"offset": offset, "limit": limit, "sort": sort, "order": order}
        return await self.http_client.get("/mentions/vulnerabilities", params=params)
