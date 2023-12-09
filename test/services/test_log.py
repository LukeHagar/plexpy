import unittest
import responses
from src.plexsdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.plexsdk.services.log import Log


class TestLog_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_log_line(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/log", json={}, status=200)
        # call the method to test
        test_service = Log("testkey")
        response = test_service.log_line("vitae", "alias", 8)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_log_line_required_fields_missing(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/log", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Log("testkey")
            test_service.log_line()
        responses.reset(),

    @responses.activate
    def test_log_line_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/log", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Log("testkey")
            test_service.log_line("non", "praesentium", 8)
        responses.reset()

    @responses.activate
    def test_log_multi_line(self):
        # Mock the API response
        responses.post("http://10.10.10.47:32400/log", json={}, status=200)
        # call the method to test
        test_service = Log("testkey")
        response = test_service.log_multi_line()
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_log_multi_line_error_on_non_200(self):
        # Mock the API response
        responses.post("http://10.10.10.47:32400/log", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Log("testkey")
            test_service.log_multi_line()
        responses.reset()

    @responses.activate
    def test_enable_paper_trail(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/log/networked", json={}, status=200)
        # call the method to test
        test_service = Log("testkey")
        response = test_service.enable_paper_trail()
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_enable_paper_trail_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/log/networked", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Log("testkey")
            test_service.enable_paper_trail()
        responses.reset()


if __name__ == "__main__":
    unittest.main()
