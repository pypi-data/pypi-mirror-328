import urllib3
from .dto import ModelConfig, ModelDetailConfig
from urllib.parse import urlparse, urlsplit


class ModelClient:
    def __init__(self, api_key: str, base_url: str = "https://api.enkryptai.com:443"):
        self.api_key = api_key
        self.base_url = base_url
        self.http = urllib3.PoolManager()
        self.headers = {"apikey": self.api_key}

    def _request(self, method, endpoint, payload=None, headers=None, **kwargs):
        url = self.base_url + endpoint
        request_headers = {
            "Accept-Encoding": "gzip",  # Add required gzip encoding
            **self.headers,
        }
        if headers:
            request_headers.update(headers)

        try:
            response = self.http.request(method, url, headers=request_headers, **kwargs)

            if response.status >= 400:
                error_response = (
                    response.json()
                    if response.data
                    else {"message": f"HTTP {response.status}"}
                )
                raise urllib3.exceptions.HTTPError(
                    f"HTTP {response.status}: {error_response}"
                )
            return response.json()
        except urllib3.exceptions.HTTPError as e:
            return {"error": str(e)}

    def health(self):
        return self._request("GET", "/models/health")

    def add_model(self, config: ModelConfig):
        """
        Add a new model configuration to the system.

        Args:
            config (ModelConfig): Configuration object containing model details

        Returns:
            dict: Response from the API containing the added model details
        """
        headers = {"Content-Type": "application/json"}
        config = ModelConfig.from_dict(config)
        # Parse endpoint_url into components
        parsed_url = urlparse(config.model_config.endpoint_url)
        path_parts = parsed_url.path.strip("/").split("/")

        # Extract base_path and endpoint path
        if len(path_parts) >= 1:
            base_path = path_parts[0]  # Usually 'v1'
            remaining_path = "/".join(path_parts[1:])  # The rest of the path
        else:
            base_path = ""
            remaining_path = ""

        # Determine paths based on the endpoint
        paths = {
            "completions": f"/{remaining_path}" if remaining_path else "",
            "chat": "",
        }

        payload = {
            "model_saved_name": config.model_saved_name,
            "testing_for": config.testing_for,
            "model_name": config.model_name,
            "model_type": config.model_type,
            "certifications": config.certifications,
            "model_config": {
                "is_compatible_with": config.model_config.is_compatible_with,
                "model_version": config.model_config.model_version,
                "hosting_type": config.model_config.hosting_type,
                "model_source": config.model_config.model_source,
                "model_provider": config.model_config.model_provider,
                "system_prompt": config.model_config.system_prompt,
                "conversation_template": config.model_config.conversation_template,
                "endpoint": {
                    "scheme": parsed_url.scheme,
                    "host": parsed_url.hostname,
                    "port": parsed_url.port
                    or (443 if parsed_url.scheme == "https" else 80),
                    "base_path": f"/{base_path}/{paths['completions']}",  # Just v1
                },
                "paths": paths,
                "auth_data": {
                    "header_name": config.model_config.auth_data.header_name,
                    "header_prefix": config.model_config.auth_data.header_prefix,
                    "space_after_prefix": config.model_config.auth_data.space_after_prefix,
                },
                "apikeys": (
                    [config.model_config.apikey] if config.model_config.apikey else []
                ),
                "default_request_options": config.model_config.default_request_options,
            },
        }
        print(payload)
        return self._request("POST", "/models/add-model", headers=headers, json=payload)

    def get_model(self, model_id: str) -> ModelConfig:
        """
        Get model configuration by model ID.

        Args:
            model_id (str): ID of the model to retrieve

        Returns:
            ModelConfig: Configuration object containing model details
        """
        headers = {"X-Enkrypt-Model": model_id}
        response = self._request("GET", "/models/get-model", headers=headers)
        return ModelConfig.from_dict(response)

    def get_model_list(self):
        """
        Get a list of all available models.

        Returns:
            dict: Response from the API containing the list of models
        """
        try:
            return self._request("GET", "/models/list-models")
        except Exception as e:
            return {"error": str(e)}

    def delete_model(self, model_id: str):
        """
        Delete a specific model from the system.

        Args:
            model_id (str): The identifier or name of the model to delete

        Returns:
            dict: Response from the API containing the deletion status
        """
        headers = {"X-Enkrypt-Model": model_id}
        return self._request("DELETE", "/models/delete-model", headers=headers)
