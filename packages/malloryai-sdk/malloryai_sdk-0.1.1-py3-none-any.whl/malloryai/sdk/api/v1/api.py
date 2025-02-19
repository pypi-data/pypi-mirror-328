from typing import Optional
import logging

from malloryai.sdk.api.v1.clients import (
    SourcesClient,
    ReferencesClient,
    ContentChunksClient,
    ThreatActorsClient,
    VulnerabilitiesClient,
    ExploitsClient,
    ExploitationsClient,
    BulletinsClient,
    DetectionSignaturesClient,
    ProductsClient,
    VendorsClient,
)
from malloryai.sdk.api.v1.http_client import HttpClient


class MalloryAPIClient:
    """Main SDK class to interact with Mallory API."""

    def __init__(self, api_key: str, logger: Optional[logging.Logger] = None):
        self.http_client = HttpClient(api_key=api_key, logger=logger)
        self.sources = SourcesClient(self.http_client)
        self.references = ReferencesClient(self.http_client)
        self.content_chunks = ContentChunksClient(self.http_client)
        self.threat_actors = ThreatActorsClient(self.http_client)
        self.vulnerabilities = VulnerabilitiesClient(self.http_client)
        self.exploits = ExploitsClient(self.http_client)
        self.exploitations = ExploitationsClient(self.http_client)
        self.bulletins = BulletinsClient(self.http_client)
        self.detection_signatures = DetectionSignaturesClient(self.http_client)
        self.products = ProductsClient(self.http_client)
        self.vendors = VendorsClient(self.http_client)
