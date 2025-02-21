"""Test cases for SecureRequest class."""

import unittest
from unittest.mock import patch, MagicMock
from secureutils.http import SecureRequest
import requests

class TestSecureRequest(unittest.TestCase):
    def setUp(self):
        self.request = SecureRequest(max_retries=2)

    @patch('requests.Session.request')
    def test_successful_request(self, mock_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.raise_for_status.return_value = None
        mock_request.return_value = mock_response

        response = self.request.get('https://example.com')
        self.assertEqual(response.status_code, 200)

    @patch('requests.Session.request')
    def test_request_with_retry(self, mock_request):
        # First call raises an error, second succeeds
        mock_request.side_effect = [
            requests.exceptions.HTTPError("Server Error", response=MagicMock(status_code=500)),
            MagicMock(status_code=200, raise_for_status=lambda: None)
        ]

        response = self.request.get('https://example.com')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mock_request.call_count, 2)

    @patch('requests.Session.request')
    def test_request_failure(self, mock_request):
        # Configure mock to always raise an exception
        mock_request.side_effect = requests.exceptions.RequestException("Test error")

        with self.assertRaises(requests.exceptions.RequestException):
            self.request.get('https://example.com')

if __name__ == '__main__':
    unittest.main()