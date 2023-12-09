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
        response = test_service.create_playlist(1, "audio", "ipsam", "ut", 4164815837)
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
            test_service.create_playlist(6, "audio", "odit", "architecto", 6469809070)
        responses.reset()

    @responses.activate
    def test_get_playlists(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/playlists/all", json={}, status=200)
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.get_playlists("audio", 2)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_playlists_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/playlists/all", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.get_playlists("audio", 3)
        responses.reset()

    @responses.activate
    def test_get_playlist(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/playlists/4535853059", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.get_playlist(4535853059)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_playlist_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/playlists/3045790262", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.get_playlist()
        responses.reset(),

    @responses.activate
    def test_get_playlist_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/playlists/6982156426", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.get_playlist(6982156426)
        responses.reset()

    @responses.activate
    def test_update_playlist(self):
        # Mock the API response
        responses.put(
            "http://10.10.10.47:32400/playlists/1213140253", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.update_playlist(1213140253)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_update_playlist_required_fields_missing(self):
        # Mock the API response
        responses.put(
            "http://10.10.10.47:32400/playlists/1991285421", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.update_playlist()
        responses.reset(),

    @responses.activate
    def test_update_playlist_error_on_non_200(self):
        # Mock the API response
        responses.put(
            "http://10.10.10.47:32400/playlists/2499309596", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.update_playlist(2499309596)
        responses.reset()

    @responses.activate
    def test_delete_playlist(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/playlists/9258358699", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.delete_playlist(9258358699)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_delete_playlist_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/playlists/3149572271", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.delete_playlist()
        responses.reset(),

    @responses.activate
    def test_delete_playlist_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/playlists/6667671900", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.delete_playlist(6667671900)
        responses.reset()

    @responses.activate
    def test_get_playlist_contents(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/playlists/6384791479/items", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.get_playlist_contents(5, 6384791479)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_playlist_contents_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/playlists/4556906109/items", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.get_playlist_contents()
        responses.reset(),

    @responses.activate
    def test_get_playlist_contents_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/playlists/8108059539/items", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.get_playlist_contents(2, 8108059539)
        responses.reset()

    @responses.activate
    def test_add_playlist_contents(self):
        # Mock the API response
        responses.put(
            "http://10.10.10.47:32400/playlists/7910596407/items", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.add_playlist_contents(7324524502, "illum", 7910596407)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_add_playlist_contents_required_fields_missing(self):
        # Mock the API response
        responses.put(
            "http://10.10.10.47:32400/playlists/7102721192/items", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.add_playlist_contents()
        responses.reset(),

    @responses.activate
    def test_add_playlist_contents_error_on_non_200(self):
        # Mock the API response
        responses.put(
            "http://10.10.10.47:32400/playlists/1070898123/items", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.add_playlist_contents(5053263185, "officiis", 1070898123)
        responses.reset()

    @responses.activate
    def test_clear_playlist_contents(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/playlists/3278852652/items", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.clear_playlist_contents(3278852652)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_clear_playlist_contents_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/playlists/5179198549/items", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.clear_playlist_contents()
        responses.reset(),

    @responses.activate
    def test_clear_playlist_contents_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/playlists/6059832913/items", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.clear_playlist_contents(6059832913)
        responses.reset()

    @responses.activate
    def test_upload_playlist(self):
        # Mock the API response
        responses.post("http://10.10.10.47:32400/playlists/upload", json={}, status=200)
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.upload_playlist(3, "cumque")
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
            test_service.upload_playlist(2, "inventore")
        responses.reset()


if __name__ == "__main__":
    unittest.main()
