import requests
import os
import json
import uuid
from typing import Dict, Any, Optional


class HostNotFoundError(Exception):
    def __init__(self, message="Host not found"):
        super().__init__(message)


class InvalidParameterError(Exception):
    pass


class HivetraceSDK:
    def __init__(self, config_path: str) -> None:
        self.hivetrace_url = self._load_hivetrace_url(config_path)
        self.session = requests.Session()

    def _load_hivetrace_url(self, config_path: str) -> str:
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"File not found")

        with open(config_path, "r") as file:
            config = json.load(file)

        hivetrace_url = config.get("hivetrace_url")
        if not hivetrace_url:
            raise HostNotFoundError()

        return hivetrace_url.rstrip("/")

    @staticmethod
    def _validate_application_id(application_id: str) -> str:
        try:
            return str(uuid.UUID(application_id))
        except ValueError as e:
            raise InvalidParameterError("Invalid application_id format") from e

    @staticmethod
    def _validate_message(message: str) -> None:
        if not isinstance(message, str) or not message.strip():
            raise InvalidParameterError("Message must be non-empty")

    @staticmethod
    def _validate_additional_parameters(
        additional_parameters: Optional[Dict[str, Any]]
    ) -> None:
        if additional_parameters is not None and not isinstance(
            additional_parameters, dict
        ):
            raise InvalidParameterError("Additional parameters must be a dict or None")

    def _send_request(
        self,
        endpoint: str,
        application_id: str,
        message: str,
        additional_parameters: Optional[Dict[str, Any]],
    ) -> Dict[str, Any]:
        try:
            application_id = self._validate_application_id(application_id)
            self._validate_message(message)
            self._validate_additional_parameters(additional_parameters)

            url = f"{self.hivetrace_url}{endpoint}"
            payload = {
                "application_id": application_id,
                "message": message,
                "additional_parameters": additional_parameters or {},
            }
            response = self.session.post(url, json=payload)
            response.raise_for_status()
            return response.json()

        except requests.RequestException:
            return {"error": "Request failed", "request_id": application_id}

    def input(
        self,
        application_id: str,
        message: str,
        additional_parameters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        return self._send_request(
            "/process_request/", application_id, message, additional_parameters
        )

    def output(
        self,
        application_id: str,
        message: str,
        additional_parameters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        return self._send_request(
            "/process_response/", application_id, message, additional_parameters
        )

    def __del__(self) -> None:
        if hasattr(self, "session"):
            self.session.close()
