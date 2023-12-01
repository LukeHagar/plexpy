import unittest
import responses
from src.plexsdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.plexsdk.services.playlists import Playlists


class TestPlaylists_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_create_playlist(self):
        # Mock the API response
        responses.post("http://10.10.10.47:32400/playlists", json={}, status=200)
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.create_playlist(
            8, "audio", "perspiciatis", "nulla", 1142710232
        )
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_create_playlist_required_fields_missing(self):
        # Mock the API response
        responses.post("http://10.10.10.47:32400/playlists", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.create_playlist()
        responses.reset(),

    @responses.activate
    def test_create_playlist_error_on_non_200(self):
        # Mock the API response
        responses.post("http://10.10.10.47:32400/playlists", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.create_playlist(
                4, "audio", "minus", "voluptatibus", 5168913335
            )
        responses.reset()

    @responses.activate
    def test_get_playlists(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/playlists/all", json={}, status=200)
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.get_playlists("audio", 7)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_playlists_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/playlists/all", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.get_playlists("audio", 8)
        responses.reset()

    @responses.activate
    def test_get_playlist(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/playlists/3834585104", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.get_playlist(3834585104)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_playlist_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/playlists/1498552017", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.get_playlist()
        responses.reset(),

    @responses.activate
    def test_get_playlist_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/playlists/3728301393", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.get_playlist(3728301393)
        responses.reset()

    @responses.activate
    def test_update_playlist(self):
        # Mock the API response
        responses.put(
            "http://10.10.10.47:32400/playlists/6463415514", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.update_playlist(6463415514)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_update_playlist_required_fields_missing(self):
        # Mock the API response
        responses.put(
            "http://10.10.10.47:32400/playlists/1892696298", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.update_playlist()
        responses.reset(),

    @responses.activate
    def test_update_playlist_error_on_non_200(self):
        # Mock the API response
        responses.put(
            "http://10.10.10.47:32400/playlists/5614438007", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.update_playlist(5614438007)
        responses.reset()

    @responses.activate
    def test_delete_playlist(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/playlists/1503931300", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.delete_playlist(1503931300)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_delete_playlist_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/playlists/6872816107", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.delete_playlist()
        responses.reset(),

    @responses.activate
    def test_delete_playlist_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/playlists/5879636257", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.delete_playlist(5879636257)
        responses.reset()

    @responses.activate
    def test_get_playlist_contents(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/playlists/8068626971/items", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.get_playlist_contents(4, 8068626971)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_playlist_contents_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/playlists/3526835986/items", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.get_playlist_contents()
        responses.reset(),

    @responses.activate
    def test_get_playlist_contents_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/playlists/7050310724/items", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.get_playlist_contents(2, 7050310724)
        responses.reset()

    @responses.activate
    def test_add_playlist_contents(self):
        # Mock the API response
        responses.put(
            "http://10.10.10.47:32400/playlists/4755754881/items", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.add_playlist_contents(5630624889, "aperiam", 4755754881)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_add_playlist_contents_required_fields_missing(self):
        # Mock the API response
        responses.put(
            "http://10.10.10.47:32400/playlists/3549730119/items", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.add_playlist_contents()
        responses.reset(),

    @responses.activate
    def test_add_playlist_contents_error_on_non_200(self):
        # Mock the API response
        responses.put(
            "http://10.10.10.47:32400/playlists/6887754067/items", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.add_playlist_contents(6059065313, "omnis", 6887754067)
        responses.reset()

    @responses.activate
    def test_clear_playlist_contents(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/playlists/2485325897/items", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.clear_playlist_contents(2485325897)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_clear_playlist_contents_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/playlists/8570406324/items", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.clear_playlist_contents()
        responses.reset(),

    @responses.activate
    def test_clear_playlist_contents_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/playlists/4469426546/items", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.clear_playlist_contents(4469426546)
        responses.reset()

    @responses.activate
    def test_upload_playlist(self):
        # Mock the API response
        responses.post("http://10.10.10.47:32400/playlists/upload", json={}, status=200)
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.upload_playlist(2, "veritatis")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_upload_playlist_required_fields_missing(self):
        # Mock the API response
        responses.post("http://10.10.10.47:32400/playlists/upload", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.upload_playlist()
        responses.reset(),

    @responses.activate
    def test_upload_playlist_error_on_non_200(self):
        # Mock the API response
        responses.post("http://10.10.10.47:32400/playlists/upload", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.upload_playlist(5, "impedit")
        responses.reset()


if __name__ == "__main__":
    unittest.main()
