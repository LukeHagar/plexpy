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
        responses.get("{protocol}://{ip}:{port}/:/scrobble", json={}, status=200)
        # call the method to test
        test_service = Media("testkey")
        response = test_service.mark_played(1)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_mark_played_required_fields_missing(self):
        # Mock the API response
        responses.get("{protocol}://{ip}:{port}/:/scrobble", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Media("testkey")
            test_service.mark_played()
        responses.reset(),

    @responses.activate
    def test_mark_played_error_on_non_200(self):
        # Mock the API response
        responses.get("{protocol}://{ip}:{port}/:/scrobble", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Media("testkey")
            test_service.mark_played(9)
        responses.reset()

    @responses.activate
    def test_mark_unplayed(self):
        # Mock the API response
        responses.get("{protocol}://{ip}:{port}/:/unscrobble", json={}, status=200)
        # call the method to test
        test_service = Media("testkey")
        response = test_service.mark_unplayed(9)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_mark_unplayed_required_fields_missing(self):
        # Mock the API response
        responses.get("{protocol}://{ip}:{port}/:/unscrobble", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Media("testkey")
            test_service.mark_unplayed()
        responses.reset(),

    @responses.activate
    def test_mark_unplayed_error_on_non_200(self):
        # Mock the API response
        responses.get("{protocol}://{ip}:{port}/:/unscrobble", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Media("testkey")
            test_service.mark_unplayed(7)
        responses.reset()

    @responses.activate
    def test_update_play_progress(self):
        # Mock the API response
        responses.post("{protocol}://{ip}:{port}/:/progress", json={}, status=200)
        # call the method to test
        test_service = Media("testkey")
        response = test_service.update_play_progress("esse", 7, "nesciunt")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_update_play_progress_required_fields_missing(self):
        # Mock the API response
        responses.post("{protocol}://{ip}:{port}/:/progress", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Media("testkey")
            test_service.update_play_progress()
        responses.reset(),

    @responses.activate
    def test_update_play_progress_error_on_non_200(self):
        # Mock the API response
        responses.post("{protocol}://{ip}:{port}/:/progress", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Media("testkey")
            test_service.update_play_progress("quo", 7, "dolorum")
        responses.reset()


if __name__ == "__main__":
    unittest.main()
