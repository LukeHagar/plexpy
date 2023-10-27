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
            6, "audio", "similique", "corporis", 9231398604
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
            test_service.create_playlist(3, "audio", "dolor", "eius", 2118287307)
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
            test_service.get_playlists("audio", 7)
        responses.reset()

    @responses.activate
    def test_get_playlist(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/playlists/1365108722", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.get_playlist(1365108722)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_playlist_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/playlists/5774434055", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.get_playlist()
        responses.reset(),

    @responses.activate
    def test_get_playlist_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/playlists/9191760374", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.get_playlist(9191760374)
        responses.reset()

    @responses.activate
    def test_update_playlist(self):
        # Mock the API response
        responses.put(
            "http://10.10.10.47:32400/playlists/5518621092", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.update_playlist(5518621092)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_update_playlist_required_fields_missing(self):
        # Mock the API response
        responses.put(
            "http://10.10.10.47:32400/playlists/9186005034", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.update_playlist()
        responses.reset(),

    @responses.activate
    def test_update_playlist_error_on_non_200(self):
        # Mock the API response
        responses.put(
            "http://10.10.10.47:32400/playlists/9820265225", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.update_playlist(9820265225)
        responses.reset()

    @responses.activate
    def test_delete_playlist(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/playlists/5260240376", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.delete_playlist(5260240376)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_delete_playlist_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/playlists/1740225155", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.delete_playlist()
        responses.reset(),

    @responses.activate
    def test_delete_playlist_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/playlists/6145805352", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.delete_playlist(6145805352)
        responses.reset()

    @responses.activate
    def test_get_playlist_contents(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/playlists/2828620637/items", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.get_playlist_contents(9, 2828620637)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_playlist_contents_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/playlists/2652525666/items", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.get_playlist_contents()
        responses.reset(),

    @responses.activate
    def test_get_playlist_contents_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/playlists/1352187138/items", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.get_playlist_contents(3, 1352187138)
        responses.reset()

    @responses.activate
    def test_add_playlist_contents(self):
        # Mock the API response
        responses.put(
            "http://10.10.10.47:32400/playlists/9135301877/items", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.add_playlist_contents(3575196026, "sit", 9135301877)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_add_playlist_contents_required_fields_missing(self):
        # Mock the API response
        responses.put(
            "http://10.10.10.47:32400/playlists/6481139604/items", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.add_playlist_contents()
        responses.reset(),

    @responses.activate
    def test_add_playlist_contents_error_on_non_200(self):
        # Mock the API response
        responses.put(
            "http://10.10.10.47:32400/playlists/2575042558/items", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.add_playlist_contents(6992293922, "excepturi", 2575042558)
        responses.reset()

    @responses.activate
    def test_clear_playlist_contents(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/playlists/5408893231/items", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.clear_playlist_contents(5408893231)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_clear_playlist_contents_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/playlists/1483530897/items", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.clear_playlist_contents()
        responses.reset(),

    @responses.activate
    def test_clear_playlist_contents_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/playlists/7836623831/items", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.clear_playlist_contents(7836623831)
        responses.reset()

    @responses.activate
    def test_upload_playlist(self):
        # Mock the API response
        responses.post("http://10.10.10.47:32400/playlists/upload", json={}, status=200)
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.upload_playlist(6, "ipsam")
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
            test_service.upload_playlist(6, "animi")
        responses.reset()


if __name__ == "__main__":
    unittest.main()
