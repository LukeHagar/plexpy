import unittest
import responses
from src.plexsdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.plexsdk.services.video import Video


class TestVideo_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_start_universal_transcode(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/video/:/transcode/universal/start.mpd",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Video("testkey")
        response = test_service.start_universal_transcode(
            "necessitatibus",
            5,
            1,
            "ut",
            8,
            6,
            5,
            8,
            8,
            "quia",
            6,
            "dicta",
            5,
            "qui",
            2,
            2,
        )
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_start_universal_transcode_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/video/:/transcode/universal/start.mpd",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = Video("testkey")
            test_service.start_universal_transcode()
        responses.reset(),

    @responses.activate
    def test_start_universal_transcode_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/video/:/transcode/universal/start.mpd",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Video("testkey")
            test_service.start_universal_transcode(
                "repellendus",
                9,
                5,
                "ea",
                7,
                4,
                1,
                1,
                3,
                "quia",
                2,
                "id",
                8,
                "cum",
                7,
                5,
            )
        responses.reset()

    @responses.activate
    def test_get_timeline(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/:/timeline", json={}, status=200)
        # call the method to test
        test_service = Video("testkey")
        response = test_service.get_timeline(
            9,
            5,
            3894342394,
            "eius illum quaerat repudiandae aspernatur",
            8,
            5,
            8,
            "playing",
            "mollitia",
            3,
        )
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_timeline_required_fields_missing(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/:/timeline", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Video("testkey")
            test_service.get_timeline()
        responses.reset(),

    @responses.activate
    def test_get_timeline_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/:/timeline", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Video("testkey")
            test_service.get_timeline(
                2,
                1,
                1592057497,
                "iure iusto id magni maxime",
                7,
                3,
                4,
                "playing",
                "maiores",
                7,
            )
        responses.reset()


if __name__ == "__main__":
    unittest.main()
