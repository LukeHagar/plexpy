import unittest
import responses
from src.plexsdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.plexsdk.services.security import Security


class TestSecurity_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_transient_token(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/security/token", json={}, status=200)
        # call the method to test
        test_service = Security("testkey")
        response = test_service.get_transient_token("all", "delegation")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_transient_token_required_fields_missing(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/security/token", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Security("testkey")
            test_service.get_transient_token()
        responses.reset(),

    @responses.activate
    def test_get_transient_token_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/security/token", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Security("testkey")
            test_service.get_transient_token("all", "delegation")
        responses.reset()

    @responses.activate
    def test_get_source_connection_information(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/security/resources", json={}, status=200
        )
        # call the method to test
        test_service = Security("testkey")
        response = test_service.get_source_connection_information("similique")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_source_connection_information_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/security/resources", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Security("testkey")
            test_service.get_source_connection_information()
        responses.reset(),

    @responses.activate
    def test_get_source_connection_information_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/security/resources", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Security("testkey")
            test_service.get_source_connection_information("facere")
        responses.reset()


if __name__ == "__main__":
    unittest.main()
