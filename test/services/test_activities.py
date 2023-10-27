import unittest
import responses
from src.plexsdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.plexsdk.services.activities import Activities


class TestActivities_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_server_activities(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/activities", json={}, status=200)
        # call the method to test
        test_service = Activities("testkey")
        response = test_service.get_server_activities()
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_server_activities_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/activities", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Activities("testkey")
            test_service.get_server_activities()
        responses.reset()

    @responses.activate
    def test_cancel_server_activities(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/activities/9191455277", json={}, status=200
        )
        # call the method to test
        test_service = Activities("testkey")
        response = test_service.cancel_server_activities("9191455277")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_cancel_server_activities_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/activities/6359244154", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Activities("testkey")
            test_service.cancel_server_activities()
        responses.reset(),

    @responses.activate
    def test_cancel_server_activities_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/activities/1590369420", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Activities("testkey")
            test_service.cancel_server_activities("1590369420")
        responses.reset()


if __name__ == "__main__":
    unittest.main()
