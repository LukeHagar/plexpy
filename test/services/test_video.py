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
            "sequi",
            9,
            2,
            "molestiae",
            2,
            2,
            8,
            1,
            5,
            "officiis",
            7,
            "incidunt",
            1,
            "iusto",
            5,
            3,
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
                "occaecati",
                6,
                9,
                "nobis",
                3,
                6,
                4,
                6,
                6,
                "provident",
                2,
                "alias",
                8,
                "eveniet",
                5,
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
            6,
            8,
            9508994071,
            "at temporibus dolorem non tempora",
            3,
            9,
            5,
            "playing",
            "itaque",
            4,
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
                5,
                6961336926,
                "recusandae tempore ullam provident incidunt",
                7,
                5,
                2,
                "playing",
                "aliquid",
                9,
            )
        responses.reset()


if __name__ == "__main__":
    unittest.main()
