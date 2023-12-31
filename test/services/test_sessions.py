import unittest
import responses
from src.plexsdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.plexsdk.services.sessions import Sessions


class TestSessions_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_sessions(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/status/sessions", json={}, status=200)
        # call the method to test
        test_service = Sessions("testkey")
        response = test_service.get_sessions()
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_sessions_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/status/sessions", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Sessions("testkey")
            test_service.get_sessions()
        responses.reset()

    @responses.activate
    def test_get_session_history(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/status/sessions/history/all", json={}, status=200
        )
        # call the method to test
        test_service = Sessions("testkey")
        response = test_service.get_session_history()
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_session_history_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/status/sessions/history/all", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Sessions("testkey")
            test_service.get_session_history()
        responses.reset()

    @responses.activate
    def test_get_transcode_sessions(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/transcode/sessions", json={}, status=200
        )
        # call the method to test
        test_service = Sessions("testkey")
        response = test_service.get_transcode_sessions()
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_transcode_sessions_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/transcode/sessions", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Sessions("testkey")
            test_service.get_transcode_sessions()
        responses.reset()

    @responses.activate
    def test_stop_transcode_session(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/transcode/sessions/nostrum", json={}, status=200
        )
        # call the method to test
        test_service = Sessions("testkey")
        response = test_service.stop_transcode_session("nostrum")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_stop_transcode_session_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/transcode/sessions/blanditiis",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = Sessions("testkey")
            test_service.stop_transcode_session()
        responses.reset(),

    @responses.activate
    def test_stop_transcode_session_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/transcode/sessions/quaerat", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Sessions("testkey")
            test_service.stop_transcode_session("quaerat")
        responses.reset()


if __name__ == "__main__":
    unittest.main()
