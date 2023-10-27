import unittest
import responses
from src.plexsdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.plexsdk.services.updater import Updater


class TestUpdater_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_update_status(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/updater/status", json={}, status=200)
        # call the method to test
        test_service = Updater("testkey")
        response = test_service.get_update_status()
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_update_status_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/updater/status", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Updater("testkey")
            test_service.get_update_status()
        responses.reset()

    @responses.activate
    def test_check_for_updates(self):
        # Mock the API response
        responses.put("http://10.10.10.47:32400/updater/check", json={}, status=200)
        # call the method to test
        test_service = Updater("testkey")
        response = test_service.check_for_updates("foo")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_check_for_updates_error_on_non_200(self):
        # Mock the API response
        responses.put("http://10.10.10.47:32400/updater/check", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Updater("testkey")
            test_service.check_for_updates("foo")
        responses.reset()

    @responses.activate
    def test_apply_updates(self):
        # Mock the API response
        responses.put("http://10.10.10.47:32400/updater/apply", json={}, status=200)
        # call the method to test
        test_service = Updater("testkey")
        response = test_service.apply_updates("foo", "foo")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_apply_updates_error_on_non_200(self):
        # Mock the API response
        responses.put("http://10.10.10.47:32400/updater/apply", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Updater("testkey")
            test_service.apply_updates("foo", "foo")
        responses.reset()


if __name__ == "__main__":
    unittest.main()
