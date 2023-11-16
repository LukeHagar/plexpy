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
            "consequuntur",
            2,
            3,
            "voluptatum",
            5,
            8,
            2,
            1,
            4,
            "a",
            8,
            "debitis",
            8,
            "non",
            7,
            5,
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
                "ut",
                9,
                3,
                "hic",
                6,
                8,
                5,
                9,
                4,
                "accusantium",
                4,
                "minima",
                6,
                "soluta",
                5,
                1,
            )
        responses.reset()

    @responses.activate
    def test_get_timeline(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/:/timeline", json={}, status=200)
        # call the method to test
        test_service = Video("testkey")
        response = test_service.get_timeline(
            8,
            9,
            5076035899,
            "nulla corporis laborum consequatur consequatur",
            4,
            6,
            7,
            "playing",
            "ipsum",
            8,
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
                4,
                3,
                8402215952,
                "nisi dolor tempore ipsum officiis",
                2,
                2,
                8,
                "playing",
                "cupiditate",
                7,
            )
        responses.reset()


if __name__ == "__main__":
    unittest.main()
