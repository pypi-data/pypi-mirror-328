import urllib3
from .dto import (
    RedTeamConfig,
    RedTeamResponse,
    RedTeamResultSummary,
    RedTeamResultDetails,
    RedTeamTaskStatus,
    RedTeamTaskDetails,
)


class RedTeamClientError(Exception):
    """
    A custom exception for Red Team errors.
    """

    pass


class RedTeamClient:
    """
    A client for interacting with the Red Team API.
    """

    def __init__(self, api_key: str, base_url: str = "https://api.enkryptai.com"):
        self.api_key = api_key
        self.base_url = base_url
        self.http = urllib3.PoolManager()
        self.headers = {"apikey": self.api_key}

    def _request(self, method, endpoint, headers=None, **kwargs):
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
                error_data = (
                    response.json()
                    if response.data
                    else {"message": f"HTTP {response.status}"}
                )
                error_message = error_data.get("message", str(error_data))
                raise urllib3.exceptions.HTTPError(error_message)
            return response.json()
        except urllib3.exceptions.HTTPError as e:
            return {"error": str(e)}

    def get_model(self, model):
        models = self._request("GET", "/models/list-models")
        if model in models:
            return model
        else:
            return None

    def add_task(
        self,
        config: RedTeamConfig,
    ):
        """
        Add a new red teaming task.
        """
        config = RedTeamConfig.from_dict(config)
        test_configs = config.redteam_test_configurations.to_dict()
        # Remove None or empty test configurations
        test_configs = {k: v for k, v in test_configs.items() if v is not None}

        payload = {
            # "async": config.async_enabled,
            "dataset_name": config.dataset_name,
            "test_name": config.test_name,
            "redteam_test_configurations": test_configs,
        }

        model = config.model_name
        saved_model = self.get_model(model)

        if saved_model:
            print("saved model found")
            headers = {
                "X-Enkrypt-Model": saved_model,
                "Content-Type": "application/json",
            }
            payload["location"] = {"storage": "supabase", "container_name": "supabase"}
            return self._request(
                "POST",
                "/redteam/v2/model/add-task",
                headers=headers,
                json=payload,
            )
        elif config.target_model_configuration:
            payload["target_model_configuration"] = (
                config.target_model_configuration.to_dict()
            )
            # print(payload)
            response = self._request(
                "POST",
                "/redteam/v2/add-task",
                json=payload,
            )
            if response.get("error"):
                raise RedTeamClientError(response["error"])
            return RedTeamResponse.from_dict(response)
        else:
            raise RedTeamClientError(
                "Please use a saved model or provide a target model configuration"
            )

    def status(self, task_id: str):
        """
        Get the status of a specific red teaming task.

        Args:
            task_id (str): The ID of the task to check status

        Returns:
            dict: The task status information
        """
        headers = {"X-Enkrypt-Task-ID": task_id}

        response = self._request("GET", "/redteam/task-status", headers=headers)
        if response.get("error"):
            raise RedTeamClientError(response["error"])
        return RedTeamTaskStatus.from_dict(response)

    def cancel_task(self, task_id: str):
        """
        Cancel a specific red teaming task.

        Args:
            task_id (str): The ID of the task to cancel
        """
        raise RedTeamClientError(
            "This feature is currently under development. Please check our documentation "
            "at https://docs.enkrypt.ai for updates or contact support@enkrypt.ai for assistance."
        )

    def get_task(self, task_id: str):
        """
        Get the status and details of a specific red teaming task.

        Args:
            task_id (str): The ID of the task to retrieve

        Returns:
            dict: The task details and status
        """
        headers = {"X-Enkrypt-Task-ID": task_id}

        response = self._request("GET", "/redteam/get-task", headers=headers)
        if response.get("error"):
            raise RedTeamClientError(response["error"])
        if response.get("data").get("job_id "):
            response["data"]["task_id"] = response["data"].pop("job_id")
        return RedTeamTaskDetails.from_dict(response["data"])

    def get_result_summary(self, task_id: str):
        """
        Get the summary of results for a specific red teaming task.

        Args:
            task_id (str): The ID of the task to get results for

        Returns:
            dict: The summary of the task results
        """
        headers = {"X-Enkrypt-Task-ID": task_id}

        response = self._request("GET", "/redteam/results/summary", headers=headers)
        if response.get("error"):
            raise RedTeamClientError(response["error"])
        return RedTeamResultSummary.from_dict(response["summary"])

    def get_result_details(self, task_id: str):
        """
        Get the detailed results for a specific red teaming task.

        Args:
            task_id (str): The ID of the task to get detailed results for

        Returns:
            dict: The detailed task results
        """
        # TODO: Update the response to be updated
        headers = {"X-Enkrypt-Task-ID": task_id}
        response = self._request("GET", "/redteam/results/details", headers=headers)
        if response.get("error"):
            raise RedTeamClientError(response["error"])
        return RedTeamResultDetails.from_dict(response["details"])
