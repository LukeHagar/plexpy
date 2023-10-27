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
        response = test_service.get_file_hash("harum", 3)
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
            test_service.get_file_hash("debitis", 9)
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
            "http://10.10.10.47:32400/library/sections/1902657001", json={}, status=200
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_library(1902657001, 6)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_library_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/3167481710", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Library("testkey")
            test_service.get_library()
        responses.reset(),

    @responses.activate
    def test_get_library_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/4877467839", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_library(4877467839, 5)
        responses.reset()

    @responses.activate
    def test_delete_library(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/library/sections/8087858304", json={}, status=200
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.delete_library(8087858304)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_delete_library_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/library/sections/3795773112", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Library("testkey")
            test_service.delete_library()
        responses.reset(),

    @responses.activate
    def test_delete_library_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/library/sections/6227875135", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.delete_library(6227875135)
        responses.reset()

    @responses.activate
    def test_get_library_items(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/6046339919/all",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_library_items(6046339919, 8, "error")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_library_items_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/4081463593/all",
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
            "http://10.10.10.47:32400/library/sections/8084937448/all",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_library_items(8084937448, 2, "sint")
        responses.reset()

    @responses.activate
    def test_refresh_library(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/5454812191/refresh",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.refresh_library(5454812191)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_refresh_library_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/7285849503/refresh",
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
            "http://10.10.10.47:32400/library/sections/3253419710/refresh",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.refresh_library(3253419710)
        responses.reset()

    @responses.activate
    def test_get_latest_library_items(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/5633500181/latest",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_latest_library_items(2, 5633500181, "similique")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_latest_library_items_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/8744481339/latest",
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
            "http://10.10.10.47:32400/library/sections/1338044693/latest",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_latest_library_items(4, 1338044693, "quo")
        responses.reset()

    @responses.activate
    def test_get_common_library_items(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/3556695926/common",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_common_library_items(7, 3556695926, "id")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_common_library_items_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/5226642550/common",
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
            "http://10.10.10.47:32400/library/sections/2153034771/common",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_common_library_items(2, 2153034771, "eos")
        responses.reset()

    @responses.activate
    def test_get_metadata(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/metadata/5", json={}, status=200
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_metadata(5)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_metadata_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/metadata/9", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Library("testkey")
            test_service.get_metadata()
        responses.reset(),

    @responses.activate
    def test_get_metadata_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/metadata/2", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_metadata(2)
        responses.reset()

    @responses.activate
    def test_get_metadata_children(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/metadata/7/children", json={}, status=200
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_metadata_children(7)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_metadata_children_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/metadata/8/children", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Library("testkey")
            test_service.get_metadata_children()
        responses.reset(),

    @responses.activate
    def test_get_metadata_children_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/metadata/2/children", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_metadata_children(2)
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
