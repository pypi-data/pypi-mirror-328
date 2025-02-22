from dataclasses import dataclass, field, asdict
from typing import Optional, List, Set, Dict, Any
from enum import Enum
import json


class Modality(Enum):
    TEXT = "text"
    IMAGE = "image"
    AUDIO = "audio"
    VIDEO = "video"

    def to_dict(self):
        return self.value


@dataclass
class EndpointConfig:
    scheme: str = "https"
    host: str = "api.openai.com"
    port: int = 443
    base_path: str = "v1"


@dataclass
class PathsConfig:
    completions: str = "/chat/completions"
    chat: str = "chat/completions"


@dataclass
class AuthData:
    header_name: str = "Authorization"
    header_prefix: str = "Bearer"
    space_after_prefix: bool = True

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)


@dataclass
class ModelDetailConfig:
    model_version: Optional[str] = None
    model_source: str = ""
    model_provider: str = "openai"
    system_prompt: str = ""

    endpoint_url: str = "https://api.openai.com/v1/chat/completions"
    auth_data: AuthData = field(default_factory=AuthData)
    api_keys: Set[Optional[str]] = field(default_factory=lambda: {None})


@dataclass
class DetailModelConfig:
    model_saved_name: str = "Model Name"
    testing_for: str = "LLM"
    model_name: str = "gpt-4o-mini"
    modality: Modality = Modality.TEXT
    model_config: ModelDetailConfig = field(default_factory=ModelDetailConfig)


@dataclass
class ModelConfigDetails:
    model_version: Optional[str] = None
    model_source: str = ""
    model_provider: str = "openai"
    system_prompt: str = ""
    conversation_template: str = ""
    is_compatible_with: str = "openai"
    hosting_type: str = "External"
    endpoint_url: str = "https://api.openai.com/v1/chat/completions"
    auth_data: AuthData = field(default_factory=AuthData)
    apikey: Optional[str] = None
    default_request_options: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict):
        # Create a copy of the data to avoid modifying the original
        data = data.copy()

        # Remove known fields that we don't want in our model
        unwanted_fields = ["queryParams", "paths"]
        for field in unwanted_fields:
            data.pop(field, None)

        # Handle apikeys to apikey conversion
        if "apikeys" in data:
            apikeys = data.pop("apikeys")
            if apikeys and not data.get("apikey"):
                data["apikey"] = apikeys[0]

        # Convert endpoint dict to endpoint_url if present
        if "endpoint" in data:
            endpoint = data.pop("endpoint")
            scheme = endpoint.get("scheme", "https")
            host = endpoint.get("host", "")
            port = endpoint.get("port", "")
            base_path = endpoint.get("base_path", "")

            endpoint_url = f"{scheme}://{host}"
            if port and port not in [80, 443]:
                endpoint_url += f":{port}"
            if base_path:
                base_path = "/" + base_path.strip("/")
                endpoint_url += base_path

            data["endpoint_url"] = endpoint_url

        # Handle nested AuthData
        auth_data = data.pop("auth_data", {})
        auth_data_obj = AuthData.from_dict(auth_data)

        # Only keep fields that are defined in the dataclass
        valid_fields = cls.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_fields}

        return cls(**filtered_data, auth_data=auth_data_obj)

    def to_dict(self):
        d = asdict(self)
        # Handle AuthData specifically
        d["auth_data"] = self.auth_data.to_dict()
        return d

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str):
        return cls.from_dict(json.loads(json_str))


@dataclass
class ModelConfig:
    created_at: str = ""
    updated_at: str = ""
    model_id: str = ""
    model_saved_name: str = "Model Name"
    testing_for: str = "LLM"
    model_name: str = "gpt-4o-mini"
    model_type: str = "text_2_text"
    modality: Modality = Modality.TEXT
    certifications: List[str] = field(default_factory=list)
    model_config: ModelConfigDetails = field(default_factory=ModelConfigDetails)

    def to_dict(self) -> dict:
        """Convert the ModelConfig instance to a dictionary."""
        # First create a shallow copy of self as dict
        d = {}
        for field in self.__dataclass_fields__:
            value = getattr(self, field)
            if field == "modality":
                d[field] = value.value
            elif field == "model_config":
                if isinstance(value, ModelConfigDetails):
                    d[field] = value.to_dict()
                else:
                    d[field] = value
            else:
                d[field] = value
        return d

    def to_json(self) -> str:
        """Convert the ModelConfig instance to a JSON string."""
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, data: dict):
        """Create a ModelConfig instance from a dictionary."""
        # Handle nested ModelConfigDetails
        model_config_data = data.pop("model_config", {})
        model_config = ModelConfigDetails.from_dict(model_config_data)

        # Handle Modality enum
        modality_value = data.pop("modality", "text")
        modality = Modality(modality_value)

        return cls(**data, modality=modality, model_config=model_config)

    @classmethod
    def from_json(cls, json_str: str):
        """Create a ModelConfig instance from a JSON string."""
        data = json.loads(json_str)
        return cls.from_dict(data)

    def __str__(self):
        """String representation of the ModelConfig."""
        return f"ModelConfig(name={self.model_saved_name}, model={self.model_name})"

    def __repr__(self):
        """Detailed string representation of the ModelConfig."""
        return (
            f"ModelConfig({', '.join(f'{k}={v!r}' for k, v in self.to_dict().items())})"
        )


# Default configuration
DETAIL_MODEL_CONFIG = ModelConfig()
