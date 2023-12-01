import unittest
import responses
from src.plexsdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.plexsdk.services.server import Server


class TestServer_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_server_capabilities(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/", json={}, status=200)
        # call the method to test
        test_service = Server("testkey")
        response = test_service.get_server_capabilities()
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_server_capabilities_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Server("testkey")
            test_service.get_server_capabilities()
        responses.reset()

    @responses.activate
    def test_get_server_preferences(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/:/prefs", json={}, status=200)
        # call the method to test
        test_service = Server("testkey")
        response = test_service.get_server_preferences()
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_server_preferences_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/:/prefs", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Server("testkey")
            test_service.get_server_preferences()
        responses.reset()

    @responses.activate
    def test_get_available_clients(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/clients", json={}, status=200)
        # call the method to test
        test_service = Server("testkey")
        response = test_service.get_available_clients()
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_available_clients_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/clients", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Server("testkey")
            test_service.get_available_clients()
        responses.reset()

    @responses.activate
    def test_get_devices(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/devices", json={}, status=200)
        # call the method to test
        test_service = Server("testkey")
        response = test_service.get_devices()
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_devices_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/devices", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Server("testkey")
            test_service.get_devices()
        responses.reset()

    @responses.activate
    def test_get_server_identity(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/identity", json={}, status=200)
        # call the method to test
        test_service = Server("testkey")
        response = test_service.get_server_identity()
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_server_identity_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/identity", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Server("testkey")
            test_service.get_server_identity()
        responses.reset()

    @responses.activate
    def test_get_my_plex_account(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/myplex/account", json={}, status=200)
        # call the method to test
        test_service = Server("testkey")
        response = test_service.get_my_plex_account()
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_my_plex_account_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/myplex/account", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Server("testkey")
            test_service.get_my_plex_account()
        responses.reset()

    @responses.activate
    def test_get_resized_photo(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/photo/:/transcode", json={}, status=200)
        # call the method to test
        test_service = Server("testkey")
        response = test_service.get_resized_photo("dolores", 3, 6, 2, 5, 5, 7927143277)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_resized_photo_required_fields_missing(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/photo/:/transcode", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Server("testkey")
            test_service.get_resized_photo()
        responses.reset(),

    @responses.activate
    def test_get_resized_photo_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/photo/:/transcode", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Server("testkey")
            test_service.get_resized_photo("laborum", 4, 5, 2, 5, 3, 3561082273)
        responses.reset()

    @responses.activate
    def test_get_server_list(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/servers", json={}, status=200)
        # call the method to test
        test_service = Server("testkey")
        response = test_service.get_server_list()
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_server_list_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/servers", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Server("testkey")
            test_service.get_server_list()
        responses.reset()


if __name__ == "__main__":
    unittest.main()
