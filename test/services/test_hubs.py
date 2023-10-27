import unittest
import responses
from src.plexsdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.plexsdk.services.hubs import Hubs


class TestHubs_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_global_hubs(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/hubs", json={}, status=200)
        # call the method to test
        test_service = Hubs("testkey")
        response = test_service.get_global_hubs(2, 2)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_global_hubs_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/hubs", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Hubs("testkey")
            test_service.get_global_hubs(7, 5)
        responses.reset()

    @responses.activate
    def test_get_library_hubs(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/hubs/sections/7302320686", json={}, status=200
        )
        # call the method to test
        test_service = Hubs("testkey")
        response = test_service.get_library_hubs(7302320686, 4, 1)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_library_hubs_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/hubs/sections/8066749835", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Hubs("testkey")
            test_service.get_library_hubs()
        responses.reset(),

    @responses.activate
    def test_get_library_hubs_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/hubs/sections/4815305500", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Hubs("testkey")
            test_service.get_library_hubs(4815305500, 9, 9)
        responses.reset()


if __name__ == "__main__":
    unittest.main()
