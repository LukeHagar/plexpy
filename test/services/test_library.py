import unittest
import responses
from src.plexsdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.plexsdk.services.library import Library


class TestLibrary_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_file_hash(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/library/hashes", json={}, status=200)
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_file_hash("harum", 1)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_file_hash_required_fields_missing(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/library/hashes", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Library("testkey")
            test_service.get_file_hash()
        responses.reset(),

    @responses.activate
    def test_get_file_hash_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/library/hashes", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_file_hash("odit", 5)
        responses.reset()

    @responses.activate
    def test_get_recently_added(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/recentlyAdded", json={}, status=200
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_recently_added()
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_recently_added_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/recentlyAdded", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_recently_added()
        responses.reset()

    @responses.activate
    def test_get_libraries(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/library/sections", json={}, status=200)
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_libraries()
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_libraries_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/library/sections", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_libraries()
        responses.reset()

    @responses.activate
    def test_get_library(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/3256589002", json={}, status=200
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_library(3256589002, 1)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_library_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/6464919098", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Library("testkey")
            test_service.get_library()
        responses.reset(),

    @responses.activate
    def test_get_library_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/2775207028", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_library(2775207028, 4)
        responses.reset()

    @responses.activate
    def test_delete_library(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/library/sections/1385425628", json={}, status=200
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.delete_library(1385425628)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_delete_library_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/library/sections/7963042669", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Library("testkey")
            test_service.delete_library()
        responses.reset(),

    @responses.activate
    def test_delete_library_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/library/sections/2022263473", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.delete_library(2022263473)
        responses.reset()

    @responses.activate
    def test_get_library_items(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/6532870666/all",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_library_items(6532870666, 4, "deleniti")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_library_items_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/9159770408/all",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = Library("testkey")
            test_service.get_library_items()
        responses.reset(),

    @responses.activate
    def test_get_library_items_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/2991563780/all",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_library_items(2991563780, 7, "consequuntur")
        responses.reset()

    @responses.activate
    def test_refresh_library(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/1684097972/refresh",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.refresh_library(1684097972)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_refresh_library_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/6307914108/refresh",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = Library("testkey")
            test_service.refresh_library()
        responses.reset(),

    @responses.activate
    def test_refresh_library_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/9930475064/refresh",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.refresh_library(9930475064)
        responses.reset()

    @responses.activate
    def test_get_latest_library_items(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/5198482436/latest",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_latest_library_items(7, 5198482436, "laboriosam")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_latest_library_items_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/3712046031/latest",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = Library("testkey")
            test_service.get_latest_library_items()
        responses.reset(),

    @responses.activate
    def test_get_latest_library_items_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/9893231515/latest",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_latest_library_items(6, 9893231515, "tenetur")
        responses.reset()

    @responses.activate
    def test_get_common_library_items(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/6498600355/common",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_common_library_items(4, 6498600355, "magnam")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_common_library_items_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/1454500772/common",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = Library("testkey")
            test_service.get_common_library_items()
        responses.reset(),

    @responses.activate
    def test_get_common_library_items_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/1462627704/common",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_common_library_items(1, 1462627704, "veniam")
        responses.reset()

    @responses.activate
    def test_get_metadata(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/metadata/4", json={}, status=200
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_metadata(4)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_metadata_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/metadata/5", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Library("testkey")
            test_service.get_metadata()
        responses.reset(),

    @responses.activate
    def test_get_metadata_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/metadata/1", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_metadata(1)
        responses.reset()

    @responses.activate
    def test_get_metadata_children(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/metadata/6/children", json={}, status=200
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_metadata_children(6)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_metadata_children_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/metadata/7/children", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Library("testkey")
            test_service.get_metadata_children()
        responses.reset(),

    @responses.activate
    def test_get_metadata_children_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/metadata/5/children", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_metadata_children(5)
        responses.reset()

    @responses.activate
    def test_get_on_deck(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/library/onDeck", json={}, status=200)
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_on_deck()
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_on_deck_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/library/onDeck", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_on_deck()
        responses.reset()


if __name__ == "__main__":
    unittest.main()
