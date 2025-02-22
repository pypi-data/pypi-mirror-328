from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional
import json


@dataclass
class RedTeamResponse:
    task_id: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)


@dataclass
class RedTeamTaskStatus:
    status: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)


@dataclass
class RedTeamTaskDetails:
    created_at: Optional[str] = None
    model_name: Optional[str] = None
    status: Optional[str] = None
    task_id: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)


@dataclass
class RedTeamResultSummary:
    test_date: Optional[str] = None
    test_name: Optional[str] = None
    dataset_name: Optional[str] = None
    model_name: Optional[str] = None
    model_endpoint_url: Optional[str] = None
    model_source: Optional[str] = None
    model_provider: Optional[str] = None
    risk_score: Optional[float] = None
    test_type: Optional[List] = None
    nist_category: Optional[List] = None
    scenario: Optional[List] = None
    category: Optional[List] = None
    attack_method: Optional[List] = None

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)


@dataclass
class RedTeamResultDetails:  # To Be Updated
    details: Optional[Dict] = None

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)


@dataclass
class AttackMethods:
    basic: List[str] = field(default_factory=lambda: ["basic"])
    advanced: Dict[str, List[str]] = field(
        default_factory=lambda: {"static": ["single_shot"], "dynamic": ["iterative"]}
    )

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)


@dataclass
class TestConfig:
    sample_percentage: int = 100
    attack_methods: AttackMethods = field(default_factory=AttackMethods)

    def to_dict(self) -> dict:
        return {
            "sample_percentage": self.sample_percentage,
            "attack_methods": self.attack_methods.to_dict(),
        }

    @classmethod
    def from_dict(cls, data: dict):
        attack_methods = AttackMethods.from_dict(data.pop("attack_methods", {}))
        return cls(**data, attack_methods=attack_methods)


@dataclass
class RedTeamTestConfigurations:
    # Basic tests
    bias_test: TestConfig = field(default=None)
    cbrn_test: TestConfig = field(default=None)
    insecure_code_test: TestConfig = field(default=None)
    toxicity_test: TestConfig = field(default=None)
    harmful_test: TestConfig = field(default=None)
    # Advanced tests
    adv_info_test: TestConfig = field(default=None)
    adv_bias_test: TestConfig = field(default=None)
    adv_command_test: TestConfig = field(default=None)

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**{k: TestConfig.from_dict(v) for k, v in data.items()})


@dataclass
class TargetModelConfiguration:
    testing_for: str = "LLM"
    model_name: str = "gpt-4o-mini"
    model_version: Optional[str] = None
    system_prompt: str = ""
    conversation_template: str = ""
    model_source: str = ""
    model_provider: str = "openai"
    model_endpoint_url: str = "https://api.openai.com/v1/chat/completions"
    model_api_key: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)


@dataclass
class RedTeamConfig:
    test_name: str = "Test Name"
    dataset_name: str = "standard"
    model_name: str = "gpt-4o-mini"
    redteam_test_configurations: RedTeamTestConfigurations = field(
        default_factory=RedTeamTestConfigurations
    )
    target_model_configuration: TargetModelConfiguration = field(
        default_factory=TargetModelConfiguration
    )

    def to_dict(self) -> dict:
        d = asdict(self)
        d["redteam_test_configurations"] = self.redteam_test_configurations.to_dict()
        d["target_model_configuration"] = self.target_model_configuration.to_dict()
        return d

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, data: dict):
        data = data.copy()
        test_configs = RedTeamTestConfigurations.from_dict(
            data.pop("redteam_test_configurations", {})
        )
        target_config = TargetModelConfiguration.from_dict(
            data.pop("target_model_configuration", {})
        )
        return cls(
            **data,
            redteam_test_configurations=test_configs,
            target_model_configuration=target_config,
        )

    @classmethod
    def from_json(cls, json_str: str):
        return cls.from_dict(json.loads(json_str))


# Default configurations
DEFAULT_REDTEAM_CONFIG = RedTeamConfig()
