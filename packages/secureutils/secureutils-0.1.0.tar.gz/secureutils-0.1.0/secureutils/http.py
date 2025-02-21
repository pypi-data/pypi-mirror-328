"""
Secure HTTP request wrapper with built-in retry mechanism and SSL verification.
"""

import requests
from typing import Any, Dict, Optional, Union
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import logging

logger = logging.getLogger(__name__)

class SecureRequest:
    def __init__(self, verify_ssl: bool = True, timeout: int = 30, max_retries: int = 3):
        """
        Initialize SecureRequest with custom settings.

        Args:
            verify_ssl (bool): Whether to verify SSL certificates
            timeout (int): Request timeout in seconds
            max_retries (int): Maximum number of retry attempts
        """
        self.session = requests.Session()
        self.timeout = timeout
        self.verify_ssl = verify_ssl

        # Configure retry strategy with improved settings
        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=0.5,
            status_forcelist=[429, 500, 502, 503, 504],  # Added 429 for rate limiting
            allowed_methods=["HEAD", "GET", "PUT", "DELETE", "OPTIONS", "TRACE", "POST"],
            respect_retry_after_header=True,
            raise_on_redirect=True,
            raise_on_status=True  # Changed to True to properly handle server errors
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def request(
        self,
        method: str,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[Any] = None,
        json: Optional[Dict] = None,
        **kwargs
    ) -> requests.Response:
        """
        Make a secure HTTP request.

        Args:
            method (str): HTTP method (GET, POST, etc.)
            url (str): Target URL
            headers (dict): Request headers
            data (Any): Request data
            json (dict): JSON data to send
            **kwargs: Additional arguments to pass to requests

        Returns:
            requests.Response: Response object

        Raises:
            requests.RequestException: For any request-related errors
        """
        try:
            kwargs.update({
                'verify': self.verify_ssl,
                'timeout': self.timeout,
                'headers': headers or {}
            })

            response = self.session.request(
                method=method,
                url=url,
                data=data,
                json=json,
                **kwargs
            )

            # Let the retry mechanism handle all status codes
            response.raise_for_status()
            return response

        except requests.RequestException as e:
            logger.error(f"Request failed: {str(e)}")
            raise

    def get(self, url: str, **kwargs) -> requests.Response:
        """Convenience method for GET requests."""
        return self.request("GET", url, **kwargs)

    def post(self, url: str, **kwargs) -> requests.Response:
        """Convenience method for POST requests."""
        return self.request("POST", url, **kwargs)

    def put(self, url: str, **kwargs) -> requests.Response:
        """Convenience method for PUT requests."""
        return self.request("PUT", url, **kwargs)

    def delete(self, url: str, **kwargs) -> requests.Response:
        """Convenience method for DELETE requests."""
        return self.request("DELETE", url, **kwargs)