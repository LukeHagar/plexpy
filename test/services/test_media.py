import unittest
import responses
from src.plexsdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.plexsdk.services.media import Media


class TestMedia_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_mark_played(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/:/scrobble", json={}, status=200)
        # call the method to test
        test_service = Media("testkey")
        response = test_service.mark_played(4)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_mark_played_required_fields_missing(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/:/scrobble", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Media("testkey")
            test_service.mark_played()
        responses.reset(),

    @responses.activate
    def test_mark_played_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/:/scrobble", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Media("testkey")
            test_service.mark_played(9)
        responses.reset()

    @responses.activate
    def test_mark_unplayed(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/:/unscrobble", json={}, status=200)
        # call the method to test
        test_service = Media("testkey")
        response = test_service.mark_unplayed(2)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_mark_unplayed_required_fields_missing(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/:/unscrobble", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Media("testkey")
            test_service.mark_unplayed()
        responses.reset(),

    @responses.activate
    def test_mark_unplayed_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/:/unscrobble", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Media("testkey")
            test_service.mark_unplayed(9)
        responses.reset()

    @responses.activate
    def test_update_play_progress(self):
        # Mock the API response
        responses.post("http://10.10.10.47:32400/:/progress", json={}, status=200)
        # call the method to test
        test_service = Media("testkey")
        response = test_service.update_play_progress("aut", 2, "harum")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_update_play_progress_required_fields_missing(self):
        # Mock the API response
        responses.post("http://10.10.10.47:32400/:/progress", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Media("testkey")
            test_service.update_play_progress()
        responses.reset(),

    @responses.activate
    def test_update_play_progress_error_on_non_200(self):
        # Mock the API response
        responses.post("http://10.10.10.47:32400/:/progress", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Media("testkey")
            test_service.update_play_progress("odio", 6, "quae")
        responses.reset()


if __name__ == "__main__":
    unittest.main()
