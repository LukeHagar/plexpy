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
            "{protocol}://{ip}:{port}/video/:/transcode/universal/start.mpd",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Video("testkey")
        response = test_service.start_universal_transcode(
            "debitis",
            5,
            6,
            "quos",
            1,
            2,
            2,
            5,
            7,
            "maiores",
            4,
            "fugit",
            9,
            "veritatis",
            5,
            3,
        )
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_start_universal_transcode_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/video/:/transcode/universal/start.mpd",
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
            "{protocol}://{ip}:{port}/video/:/transcode/universal/start.mpd",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Video("testkey")
            test_service.start_universal_transcode(
                "quos",
                2,
                9,
                "cupiditate",
                4,
                5,
                7,
                6,
                5,
                "eligendi",
                9,
                "eum",
                9,
                "veritatis",
                8,
                2,
            )
        responses.reset()

    @responses.activate
    def test_get_timeline(self):
        # Mock the API response
        responses.get("{protocol}://{ip}:{port}/:/timeline", json={}, status=200)
        # call the method to test
        test_service = Video("testkey")
        response = test_service.get_timeline(
            1, 3, 4519717282, "neque optio ipsa aut est", 2, 6, 3, "playing", "aut", 6
        )
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_timeline_required_fields_missing(self):
        # Mock the API response
        responses.get("{protocol}://{ip}:{port}/:/timeline", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Video("testkey")
            test_service.get_timeline()
        responses.reset(),

    @responses.activate
    def test_get_timeline_error_on_non_200(self):
        # Mock the API response
        responses.get("{protocol}://{ip}:{port}/:/timeline", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Video("testkey")
            test_service.get_timeline(
                9,
                1,
                6697392847,
                "repellendus odio inventore dolore excepturi",
                6,
                4,
                4,
                "playing",
                "recusandae",
                4,
            )
        responses.reset()


if __name__ == "__main__":
    unittest.main()
