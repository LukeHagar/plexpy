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
        responses.post("{protocol}://{ip}:{port}/playlists", json={}, status=200)
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.create_playlist(
            8, "audio", "quasi", "alias", 5922730203
        )
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_create_playlist_required_fields_missing(self):
        # Mock the API response
        responses.post("{protocol}://{ip}:{port}/playlists", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.create_playlist()
        responses.reset(),

    @responses.activate
    def test_create_playlist_error_on_non_200(self):
        # Mock the API response
        responses.post("{protocol}://{ip}:{port}/playlists", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.create_playlist(4, "audio", "nihil", "cumque", 5164878131)
        responses.reset()

    @responses.activate
    def test_get_playlists(self):
        # Mock the API response
        responses.get("{protocol}://{ip}:{port}/playlists/all", json={}, status=200)
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.get_playlists("audio", 5)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_playlists_error_on_non_200(self):
        # Mock the API response
        responses.get("{protocol}://{ip}:{port}/playlists/all", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.get_playlists("audio", 4)
        responses.reset()

    @responses.activate
    def test_get_playlist(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/playlists/8961898762", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.get_playlist(8961898762)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_playlist_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/playlists/2350925795", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.get_playlist()
        responses.reset(),

    @responses.activate
    def test_get_playlist_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/playlists/7803831874", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.get_playlist(7803831874)
        responses.reset()

    @responses.activate
    def test_update_playlist(self):
        # Mock the API response
        responses.put(
            "{protocol}://{ip}:{port}/playlists/4846174885", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.update_playlist(4846174885)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_update_playlist_required_fields_missing(self):
        # Mock the API response
        responses.put(
            "{protocol}://{ip}:{port}/playlists/3217640966", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.update_playlist()
        responses.reset(),

    @responses.activate
    def test_update_playlist_error_on_non_200(self):
        # Mock the API response
        responses.put(
            "{protocol}://{ip}:{port}/playlists/2969411689", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.update_playlist(2969411689)
        responses.reset()

    @responses.activate
    def test_delete_playlist(self):
        # Mock the API response
        responses.delete(
            "{protocol}://{ip}:{port}/playlists/9157110662", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.delete_playlist(9157110662)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_delete_playlist_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "{protocol}://{ip}:{port}/playlists/9590435699", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.delete_playlist()
        responses.reset(),

    @responses.activate
    def test_delete_playlist_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "{protocol}://{ip}:{port}/playlists/7937977423", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.delete_playlist(7937977423)
        responses.reset()

    @responses.activate
    def test_get_playlist_contents(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/playlists/5686140716/items", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.get_playlist_contents(8, 5686140716)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_playlist_contents_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/playlists/3666405994/items", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.get_playlist_contents()
        responses.reset(),

    @responses.activate
    def test_get_playlist_contents_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/playlists/9239392917/items", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.get_playlist_contents(4, 9239392917)
        responses.reset()

    @responses.activate
    def test_add_playlist_contents(self):
        # Mock the API response
        responses.put(
            "{protocol}://{ip}:{port}/playlists/2224463633/items", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.add_playlist_contents(
            7330486290, "provident", 2224463633
        )
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_add_playlist_contents_required_fields_missing(self):
        # Mock the API response
        responses.put(
            "{protocol}://{ip}:{port}/playlists/8938618789/items", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.add_playlist_contents()
        responses.reset(),

    @responses.activate
    def test_add_playlist_contents_error_on_non_200(self):
        # Mock the API response
        responses.put(
            "{protocol}://{ip}:{port}/playlists/7136237365/items", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.add_playlist_contents(3430294919, "aspernatur", 7136237365)
        responses.reset()

    @responses.activate
    def test_clear_playlist_contents(self):
        # Mock the API response
        responses.delete(
            "{protocol}://{ip}:{port}/playlists/6699998436/items", json={}, status=200
        )
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.clear_playlist_contents(6699998436)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_clear_playlist_contents_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "{protocol}://{ip}:{port}/playlists/1772875063/items", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.clear_playlist_contents()
        responses.reset(),

    @responses.activate
    def test_clear_playlist_contents_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "{protocol}://{ip}:{port}/playlists/3406600816/items", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.clear_playlist_contents(3406600816)
        responses.reset()

    @responses.activate
    def test_upload_playlist(self):
        # Mock the API response
        responses.post("{protocol}://{ip}:{port}/playlists/upload", json={}, status=200)
        # call the method to test
        test_service = Playlists("testkey")
        response = test_service.upload_playlist(2, "dignissimos")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_upload_playlist_required_fields_missing(self):
        # Mock the API response
        responses.post("{protocol}://{ip}:{port}/playlists/upload", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Playlists("testkey")
            test_service.upload_playlist()
        responses.reset(),

    @responses.activate
    def test_upload_playlist_error_on_non_200(self):
        # Mock the API response
        responses.post("{protocol}://{ip}:{port}/playlists/upload", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Playlists("testkey")
            test_service.upload_playlist(5, "fugit")
        responses.reset()


if __name__ == "__main__":
    unittest.main()
