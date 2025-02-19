import copy

# Base default configuration for all detectors.
DEFAULT_CONFIG = {
    "topic_detector": {"enabled": False, "topic": []},
    "nsfw": {"enabled": False},
    "toxicity": {"enabled": False},
    "pii": {"enabled": False, "entities": []},
    "injection_attack": {"enabled": False},
    "keyword_detector": {"enabled": False, "banned_keywords": []},
    "policy_violation": {"enabled": False, "policy_text": "", "need_explanation": False},
    "bias": {"enabled": False},
    "copyright_ip": {"enabled": False},
    "system_prompt": {"enabled": False, "index": "system"}
}


class GuardrailsConfig:
    """
    A helper class to manage Guardrails configuration.

    Users can either use preset configurations or build a custom one.
    """

    def __init__(self, config=None):
        # Use a deep copy of the default to avoid accidental mutation.
        self.config = copy.deepcopy(DEFAULT_CONFIG) if config is None else config

    @classmethod
    def injection_attack(cls):
        """
        Returns a configuration instance pre-configured for injection attack detection.
        """
        config = copy.deepcopy(DEFAULT_CONFIG)
        config["topic_detector"] = {"enabled": True, "topic": ["injection attack"]}
        config["injection_attack"] = {"enabled": True}
        return cls(config)

    @classmethod
    def policy_violation(cls, policy_text: str, need_explanation: bool = False):
        """
        Returns a configuration instance pre-configured for policy violation detection.
        """
        config = copy.deepcopy(DEFAULT_CONFIG)
        config["policy_violation"] = {"enabled": True, 
                                      "policy_text": policy_text, 
                                      "need_explanation": need_explanation
                                      }
        return cls(config)

    def update(self, **kwargs):
        """
        Update the configuration with custom values.
        
        Only keys that exist in the default configuration can be updated.
        For example:
            config.update(nsfw={"enabled": True}, toxicity={"enabled": True})
        """
        for key, value in kwargs.items():
            if key in self.config:
                self.config[key] = value
            else:
                raise ValueError(f"Unknown detector config: {key}")
        return self

    def as_dict(self):
        """
        Return the underlying configuration dictionary.
        """
        return self.config
