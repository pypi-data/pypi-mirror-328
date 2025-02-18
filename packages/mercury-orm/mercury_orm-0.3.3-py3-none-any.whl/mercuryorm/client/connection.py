"""
This module contains the `ZendeskAPIClient` class responsible for
handling requests to the Zendesk API.
"""

import os
import json
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv  # pylint: disable=import-error


load_dotenv()


class ZendeskAPIClient:
    """
    A client to interact with the Zendesk API, supporting basic CRUD operations.
    """

    def __init__(self, email=os.getenv("ZENDESK_EMAIL", "mock@mock.com")):
        """
        Initializes the ZendeskAPIClient with authentication details.

        Args:
            email (str): The email associated with the Zendesk account
            (default: from environment variable).
        """
        self.email = email
        self.api_token = os.getenv("ZENDESK_API_TOKEN", "mock_token")
        self.base_url = (
            f"https://{os.getenv('ZENDESK_SUBDOMAIN', 'mockdomain')}.zendesk.com/api/v2"
        )
        self.headers = {"Content-Type": "application/json"}
        self.auth = HTTPBasicAuth(f"{self.email}/token", self.api_token)
        self.default_params = {"locale": "en"}

    def get(self, endpoint, params=None, timeout=10):
        """
        Sends a GET request to the Zendesk API.

        Args:
            endpoint (str): The API endpoint to make the GET request to.
            params (dict, optional): The query parameters for the request.
            timeout (int, optional): Timeout in seconds for the request.

        Returns:
            dict: The JSON response from the Zendesk API.

        Raises:
            requests.exceptions.HTTPError: If the request fails.
        """
        params = {**self.default_params, **(params or {})}
        response = requests.get(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            params=params,
            auth=self.auth,
            timeout=timeout,
        )
        response.raise_for_status()
        try:
            return response.json()
        except json.JSONDecodeError as json_error:
            return {
                "error": {"title": response.text, "message": str(json_error)},
                "status_code": response.status_code,
            }

    def post(self, endpoint, data, params=None, timeout=10):
        """
        Sends a POST request to the Zendesk API.

        Args:
            endpoint (str): The API endpoint to make the POST request to.
            data (dict): The JSON payload to send in the request.
            timeout (int, optional): Timeout in seconds for the request.

        Returns:
            dict: The JSON response from the Zendesk API.

        Raises:
            requests.exceptions.HTTPError: If the request fails.
        """
        params = {**self.default_params, **(params or {})}
        response = requests.post(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            json=data,
            auth=self.auth,
            timeout=timeout,
            params=params,
        )
        try:
            data = response.json()
            if not response.ok:
                data.update({"status_code": response.status_code})
            return data
        except json.JSONDecodeError as json_error:
            return {
                "error": {"title": response.text, "message": str(json_error)},
                "status_code": response.status_code,
            }

    def patch(self, endpoint, data, timeout=10, params=None):
        """
        Sends a PATCH request to the Zendesk API.

        Args:
            endpoint (str): The API endpoint to make the PATCH request to.
            data (dict): The JSON payload to send in the request.
            timeout (int, optional): Timeout in seconds for the request.

        Returns:
            dict: The JSON response from the Zendesk API.

        Raises:
            requests.exceptions.HTTPError: If the request fails.
        """
        params = {**self.default_params, **(params or {})}
        response = requests.patch(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            json=data,
            auth=self.auth,
            timeout=timeout,
            params=params,
        )
        try:
            data = response.json()
            if not response.ok:
                data.update({"status_code": response.status_code})
            return data
        except json.JSONDecodeError as json_error:
            return {
                "error": {"title": response.text, "message": str(json_error)},
                "status_code": response.status_code,
            }

    def put(self, endpoint, data, timeout=10, params=None):
        """
        Sends a PUT request to the Zendesk API.

        Args:
            endpoint (str): The API endpoint to make the PUT request to.
            data (dict): The JSON payload to send in the request.
            timeout (int, optional): Timeout in seconds for the request.

        Returns:
            dict: The JSON response from the Zendesk API.

        Raises:
            requests.exceptions.HTTPError: If the request fails.
        """
        params = {**self.default_params, **(params or {})}
        response = requests.put(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            json=data,
            auth=self.auth,
            timeout=timeout,
            params=params,
        )
        try:
            data = response.json()
            if not response.ok:
                data.update({"status_code": response.status_code})
            return data
        except json.JSONDecodeError as json_error:
            return {
                "error": {"title": response.text, "message": str(json_error)},
                "status_code": response.status_code,
            }

    def delete(self, endpoint, timeout=10, params=None):
        """
        Sends a DELETE request to the Zendesk API.

        Args:
            endpoint (str): The API endpoint to make the DELETE request to.
            timeout (int, optional): Timeout in seconds for the request.

        Returns:
            dict: The JSON response from the Zendesk API, including the status code.

        Raises:
            requests.exceptions.HTTPError: If the request fails.
        """
        params = {**self.default_params, **(params or {})}
        response = requests.delete(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            auth=self.auth,
            timeout=timeout,
            params=params,
        )
        if response.status_code == 204:
            return {"status_code": 204}
        try:
            data = response.json()
            if not response.ok:
                data.update({"status_code": response.status_code})
            return data
        except json.JSONDecodeError as json_error:
            return {
                "error": {"title": response.text, "message": str(json_error)},
                "status_code": response.status_code,
            }

    def upload_file(self, filename: str, content: bytes, timeout: int = 10) -> dict:
        """
        Uploads a file to Zendesk.
        """
        response = requests.post(
            f"{self.base_url}/uploads",
            headers={"Content-Type": "application/binary"},
            data=content,
            auth=self.auth,
            params={"filename": filename},
            timeout=timeout,
        )
        response.raise_for_status()
        return response.json()
