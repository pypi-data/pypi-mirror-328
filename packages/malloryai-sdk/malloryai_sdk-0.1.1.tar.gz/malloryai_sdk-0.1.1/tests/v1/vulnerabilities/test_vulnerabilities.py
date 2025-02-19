import pytest

pytestmark = pytest.mark.asyncio


async def test_list_vulnerabilities(api_client):
    """Test list_vulnerabilities() API call."""
    response = await api_client.vulnerabilities.list_vulnerabilities()

    assert isinstance(response, dict), "Response is not a dictionary"
    assert "data" in response and isinstance(
        response["data"], list
    ), "Missing expected field: data"

    if response["data"]:
        first_vuln = response["data"][0]
        assert "cve_id" in first_vuln, "Missing expected field: cve_id"
        assert "description" in first_vuln, "Missing expected field: description"
        assert (
            "cvss_3_base_severity" in first_vuln
        ), "Missing expected field: cvss_3_base_severity"


async def test_get_vulnerability(api_client):
    """Test get_vulnerability() API call."""
    vulnerability = await api_client.vulnerabilities.list_vulnerabilities(limit=1)
    assert isinstance(vulnerability, dict), "Response is not a dictionary"
    assert vulnerability["data"], "No vulnerabilities found to test with"
    vuln_id = vulnerability["data"][0]["cve_id"]
    response = await api_client.vulnerabilities.get_vulnerability(vuln_id)

    assert isinstance(response, dict)

    assert response["cve_id"] == vuln_id, "CVE ID does not match"
    assert "description" in response, "Missing expected field: description"
    assert "cvss_3_base_score" in response, "Missing expected field: cvss_3_base_score"
    assert (
        "cvss_3_base_severity" in response
    ), "Missing expected field: cvss_3_base_severity"


async def test_get_vulnerability_configurations(api_client):
    """Test get_vulnerability_configurations() API call."""
    vulnerability = await api_client.vulnerabilities.list_vulnerabilities(limit=1)
    assert isinstance(vulnerability, dict), "Response is not a dictionary"
    assert vulnerability["data"], "No vulnerabilities found to test with"
    vuln_id = vulnerability["data"][0]["cve_id"]
    response = await api_client.vulnerabilities.get_vulnerability_configurations(
        vuln_id
    )

    if not response:
        pytest.skip("No configurations found for this vulnerability")

    assert isinstance(response, list), "Response is not a list"
    if response:
        first_config = response[0]
        required_fields = [
            "uuid",
            "created_at",
            "updated_at",
            "cpe_id",
            "set_id",
            "edition",
            "language",
            "sw_edition",
            "target_sw",
            "target_hw",
            "other",
            "versionStartExcluding",
            "versionStartIncluding",
            "versionEndExcluding",
            "versionEndIncluding",
            "updateStartIncluding",
            "updateEndIncluding",
            "is_vulnerable",
            "vendor",
            "vendor_display_name",
            "product_type",
            "product",
            "product_display_name",
            "cve_id",
        ]

        for field in required_fields:
            assert field in first_config, f"Missing expected field: {field}"


async def test_get_vulnerability_detection_signatures(api_client):
    """Test get_vulnerability_detection_signatures() API call."""
    vulnerability = await api_client.vulnerabilities.list_vulnerabilities(limit=1)
    assert isinstance(vulnerability, dict), "Response is not a dictionary"
    assert vulnerability["data"], "No vulnerabilities found to test with"
    vuln_id = vulnerability["data"][0]["cve_id"]
    response = await api_client.vulnerabilities.get_vulnerability_detection_signatures(
        vuln_id
    )

    if not response:
        pytest.skip("No detection signatures found for this vulnerability")

    assert isinstance(response, list), "Response is not a list"
    if response:
        first_config = response[0]
        required_fields = []

        for field in required_fields:
            assert field in first_config, f"Missing expected field: {field}"


async def test_get_vulnerability_exploitations(api_client):
    """Test get_vulnerability_exploitations() API call."""
    vulnerability = await api_client.vulnerabilities.list_vulnerabilities(limit=1)
    assert isinstance(vulnerability, dict), "Response is not a dictionary"
    assert vulnerability["data"], "No vulnerabilities found to test with"
    vuln_id = vulnerability["data"][0]["cve_id"]
    response = await api_client.vulnerabilities.get_vulnerability_exploitations(vuln_id)

    if not response:
        pytest.skip("No exploitations found for this vulnerability")

    assert isinstance(response, list), "Response is not a list"
    if response:
        first_config = response[0]
        required_fields = []

        for field in required_fields:
            assert field in first_config, f"Missing expected field: {field}"


async def test_get_vulnerability_exploits(api_client):
    """Test get_vulnerability_exploits() API call."""
    vulnerability = await api_client.vulnerabilities.list_vulnerabilities(limit=1)
    assert isinstance(vulnerability, dict), "Response is not a dictionary"
    assert vulnerability["data"], "No vulnerabilities found to test with"
    vuln_id = vulnerability["data"][0]["cve_id"]
    response = await api_client.vulnerabilities.get_vulnerability_exploits(vuln_id)

    if not response:
        pytest.skip("No exploitations found for this vulnerability")

    assert isinstance(response, list), "Response is not a list"
    if response:
        first_config = response[0]
        required_fields = [
            "uuid",
            "description",
            "url",
            "maturity",
            "created_at",
            "updated_at",
            "vulnerabilities",
        ]

        for field in required_fields:
            assert field in first_config, f"Missing expected field: {field}"


async def test_get_vulnerability_mentions(api_client):
    """Test get_vulnerability_mentions() API call."""
    vulnerability = await api_client.vulnerabilities.list_vulnerabilities(limit=1)
    assert isinstance(vulnerability, dict), "Response is not a dictionary"
    assert vulnerability["data"], "No vulnerabilities found to test with"
    vuln_id = vulnerability["data"][0]["cve_id"]
    response = await api_client.vulnerabilities.get_vulnerability_mentions(vuln_id)

    if not response:
        pytest.skip("No mentions found for this vulnerability")

    assert isinstance(response, list), "Response is not a list"
    if response:
        first_config = response[0]
        required_fields = []

        for field in required_fields:
            assert field in first_config, f"Missing expected field: {field}"


async def test_get_vulnerabilities_mentions(api_client):
    """Test get_vulnerabilities_mentions() API call."""
    response = await api_client.vulnerabilities.list_vulnerabilities_mentions(limit=5)

    assert isinstance(response, dict)
    assert "data" in response and isinstance(
        response["data"], list
    ), "Missing expected field: data"
    assert "total" in response and isinstance(
        response["total"], int
    ), "Missing expected field: total"
    assert "offset" in response and isinstance(
        response["offset"], int
    ), "Missing expected field: offset"
    assert "limit" in response and isinstance(
        response["limit"], int
    ), "Missing expected field: limit"

    if response["data"]:  # If results exist, validate structure of first entry
        first_config = response["data"][0]
        required_fields = [
            "uuid",
            "created_at",
            "updated_at",
            "overview",
            "content_chunk_uuid",
            "reference_uuid",
            "reference_url",
            "vulnerability_uuid",
            "cve_id",
        ]

        for field in required_fields:
            assert field in first_config, f"Missing expected field: {field}"


async def test_list_vulnerable_configurations(api_client):
    """Test list_vulnerable_configurations() API call."""
    response = await api_client.vulnerabilities.list_vulnerable_configurations(limit=5)

    assert isinstance(response, dict), "Response is not a dictionary"
    assert "data" in response and isinstance(
        response["data"], list
    ), "Missing expected field: data"
    assert "total" in response and isinstance(
        response["total"], int
    ), "Missing expected field: total"
    assert "offset" in response and isinstance(
        response["offset"], int
    ), "Missing expected field: offset"
    assert "limit" in response and isinstance(
        response["limit"], int
    ), "Missing expected field: limit"

    if response["data"]:  # If results exist, validate structure of first entry
        first_config = response["data"][0]
        required_fields = [
            "uuid",
            "created_at",
            "updated_at",
            "cpe_id",
            "set_id",
            "edition",
            "language",
            "sw_edition",
            "target_sw",
            "target_hw",
            "other",
            "versionStartExcluding",
            "versionStartIncluding",
            "versionEndExcluding",
            "versionEndIncluding",
            "updateStartIncluding",
            "updateEndIncluding",
            "is_vulnerable",
            "vendor",
            "vendor_display_name",
            "product_type",
            "product",
            "product_display_name",
            "cve_id",
        ]

        for field in required_fields:
            assert field in first_config, f"Missing expected field: {field}"
