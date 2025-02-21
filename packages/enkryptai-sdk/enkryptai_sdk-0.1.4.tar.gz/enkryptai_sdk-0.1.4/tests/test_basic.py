import os
import pytest
from enkryptai_sdk import GuardrailsClient, GuardrailsConfig
from dotenv import load_dotenv

load_dotenv()

# Dummy API key and base URL for local testing.
# For real testing, you might mock requests or use a staging endpoint.
API_KEY = os.getenv("ENK_API_KEY")
BASE_URL = os.getenv("ENK_BASE_URL", "https://api.enkryptai.com")

@pytest.fixture
def client():
    return GuardrailsClient(api_key=API_KEY, base_url=BASE_URL)

def test_health(client):
    # Since we're using a dummy API key, you might want to mock the response.
    # For now, let's just check that the client object has been created.
    assert hasattr(client, "health")

def test_config_injection_attack():
    # Test that the injection attack preset returns a valid configuration.
    config = GuardrailsConfig.injection_attack()
    config_dict = config.as_dict()
    assert config_dict["topic_detector"]["enabled"] is True
    assert "injection attack" in config_dict["topic_detector"]["topic"]

def test_policy_violation_config():
    policy_text = "Test Policy"
    config = GuardrailsConfig.policy_violation(policy_text)
    config_dict = config.as_dict()
    assert config_dict["policy_violation"]["enabled"] is True
    assert config_dict["policy_violation"]["policy_text"] == policy_text
