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
        responses.get("{protocol}://{ip}:{port}/hubs", json={}, status=200)
        # call the method to test
        test_service = Hubs("testkey")
        response = test_service.get_global_hubs(8, 4)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_global_hubs_error_on_non_200(self):
        # Mock the API response
        responses.get("{protocol}://{ip}:{port}/hubs", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Hubs("testkey")
            test_service.get_global_hubs(8, 3)
        responses.reset()

    @responses.activate
    def test_get_library_hubs(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/hubs/sections/3684333305", json={}, status=200
        )
        # call the method to test
        test_service = Hubs("testkey")
        response = test_service.get_library_hubs(3684333305, 2, 4)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_library_hubs_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/hubs/sections/2635728470", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Hubs("testkey")
            test_service.get_library_hubs()
        responses.reset(),

    @responses.activate
    def test_get_library_hubs_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/hubs/sections/5770327453", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Hubs("testkey")
            test_service.get_library_hubs(5770327453, 9, 3)
        responses.reset()


if __name__ == "__main__":
    unittest.main()
