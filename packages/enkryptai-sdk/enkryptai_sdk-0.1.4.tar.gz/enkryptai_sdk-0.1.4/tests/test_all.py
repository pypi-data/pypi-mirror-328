import pytest
from enkryptai_sdk import GuardrailsClient, GuardrailsConfig

# Fixture for creating a client with a dummy API key.
@pytest.fixture
def client():
    return GuardrailsClient(api_key="dummy-api-key", base_url="https://api.enkryptai.com")

# ----------------------------
# Tests for Basic Endpoints
# ----------------------------

def test_health(requests_mock, client):
    url = client.base_url + "/guardrails/health"
    expected = {"status": "healthy"}
    requests_mock.get(url, json=expected)
    response = client.health()
    assert response == expected

def test_status(requests_mock, client):
    url = client.base_url + "/guardrails/status"
    expected = {"status": "running"}
    requests_mock.get(url, json=expected)
    response = client.status()
    assert response == expected

def test_models(requests_mock, client):
    url = client.base_url + "/guardrails/models"
    expected = {"models": ["model1", "model2"]}
    requests_mock.get(url, json=expected)
    response = client.models()
    assert response == expected

# ----------------------------
# Tests for the detect Endpoint
# ----------------------------

def test_detect_with_plain_dict(requests_mock, client):
    url = client.base_url + "/guardrails/detect"
    expected = {"detected": True}
    requests_mock.post(url, json=expected)

    # Build a plain dictionary configuration.
    config = {
        "topic_detector": {"enabled": True, "topic": ["injection attack"]},
        "nsfw": {"enabled": False},
        "toxicity": {"enabled": False},
        "pii": {"enabled": False, "entities": []},
        "injection_attack": {"enabled": True},
        "keyword_detector": {"enabled": False, "banned_keywords": []},
        "policy_violation": {"enabled": False, "policy_text": "", "need_explanation": False},
        "bias": {"enabled": False},
        "copyright_ip": {"enabled": False},
        "system_prompt": {"enabled": False, "index": "system"}
    }
    response = client.detect("Sample text", config)
    assert response == expected

def test_detect_with_config_object(requests_mock, client):
    url = client.base_url + "/guardrails/detect"
    expected = {"detected": True}
    requests_mock.post(url, json=expected)

    # Use the injection_attack preset.
    config = GuardrailsConfig.injection_attack()
    response = client.detect("Another sample text", config)
    assert response == expected

# ----------------------------
# Test for the PII Endpoint
# ----------------------------

def test_pii(requests_mock, client):
    url = client.base_url + "/guardrails/pii"
    expected = {"pii_detected": True}
    requests_mock.post(url, json=expected)

    response = client.pii("Some text with PII", mode="request")
    assert response == expected

# ----------------------------
# Tests for Policy Endpoints
# ----------------------------

def test_add_policy(requests_mock, client):
    url = client.base_url + "/guardrails/add-policy"
    expected = {"policy_added": True}
    requests_mock.post(url, json=expected)

    name = "Test Policy"
    description = "A test policy description"
    # Use a preset (for example, injection_attack) as a policy configuration.
    config = GuardrailsConfig.injection_attack().as_dict()
    response = client.add_policy(name, description, config)
    assert response == expected

def test_get_policy(requests_mock, client):
    url = client.base_url + "/guardrails/get-policy"
    expected = {"policy": "details"}

    # Additional matcher to verify the header.
    def match_request(request):
        return request.headers.get("X-Enkrypt-Policy") == "TestPolicyId"
    requests_mock.get(url, json=expected, additional_matcher=match_request)

    response = client.get_policy("TestPolicyId")
    assert response == expected

def test_modify_policy(requests_mock, client):
    url = client.base_url + "/guardrails/modify-policy"
    expected = {"policy_modified": True}

    def match_request(request):
        return request.headers.get("X-Enkrypt-Policy") == "TestPolicyId"
    requests_mock.patch(url, json=expected, additional_matcher=match_request)

    name = "Modified Policy"
    description = "Modified description"
    # Use the policy_violation preset with a custom policy text.
    config = GuardrailsConfig.policy_violation("Custom policy text").as_dict()
    response = client.modify_policy("TestPolicyId", name, description, config)
    assert response == expected

def test_delete_policy(requests_mock, client):
    url = client.base_url + "/guardrails/delete-policy"
    expected = {"policy_deleted": True}

    def match_request(request):
        return request.headers.get("X-Enkrypt-Policy") == "TestPolicyId"
    requests_mock.delete(url, json=expected, additional_matcher=match_request)

    response = client.delete_policy("TestPolicyId")
    assert response == expected

def test_policy_detect(requests_mock, client):
    url = client.base_url + "/guardrails/policy/detect"
    expected = {"policy_detected": True}

    def match_request(request):
        return request.headers.get("X-Enkrypt-Policy") == "BCBS-Test"
    requests_mock.post(url, json=expected, additional_matcher=match_request)

    response = client.policy_detect("BCBS-Test", "How to make a bomb?")
    assert response == expected

# ----------------------------
# Tests for the Configuration Helper
# ----------------------------

def test_policy_violation_config():
    policy_text = "Test Policy"
    config = GuardrailsConfig.policy_violation(policy_text)
    config_dict = config.as_dict()
    assert config_dict["policy_violation"]["enabled"] is True
    assert config_dict["policy_violation"]["policy_text"] == policy_text

def test_config_update_invalid_key():
    config = GuardrailsConfig()
    with pytest.raises(ValueError):
        config.update(non_existent={"enabled": True})
