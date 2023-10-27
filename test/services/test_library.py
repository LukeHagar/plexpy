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
        responses.get("{protocol}://{ip}:{port}/library/hashes", json={}, status=200)
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_file_hash("asperiores", 7)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_file_hash_required_fields_missing(self):
        # Mock the API response
        responses.get("{protocol}://{ip}:{port}/library/hashes", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Library("testkey")
            test_service.get_file_hash()
        responses.reset(),

    @responses.activate
    def test_get_file_hash_error_on_non_200(self):
        # Mock the API response
        responses.get("{protocol}://{ip}:{port}/library/hashes", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_file_hash("cum", 4)
        responses.reset()

    @responses.activate
    def test_get_recently_added(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/library/recentlyAdded", json={}, status=200
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
            "{protocol}://{ip}:{port}/library/recentlyAdded", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_recently_added()
        responses.reset()

    @responses.activate
    def test_get_libraries(self):
        # Mock the API response
        responses.get("{protocol}://{ip}:{port}/library/sections", json={}, status=200)
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_libraries()
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_libraries_error_on_non_200(self):
        # Mock the API response
        responses.get("{protocol}://{ip}:{port}/library/sections", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_libraries()
        responses.reset()

    @responses.activate
    def test_get_library(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/library/sections/9871766595", json={}, status=200
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_library(9871766595, 8)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_library_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/library/sections/5100915384", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Library("testkey")
            test_service.get_library()
        responses.reset(),

    @responses.activate
    def test_get_library_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/library/sections/6801308709", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_library(6801308709, 3)
        responses.reset()

    @responses.activate
    def test_delete_library(self):
        # Mock the API response
        responses.delete(
            "{protocol}://{ip}:{port}/library/sections/3061349599", json={}, status=200
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.delete_library(3061349599)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_delete_library_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "{protocol}://{ip}:{port}/library/sections/6921817889", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Library("testkey")
            test_service.delete_library()
        responses.reset(),

    @responses.activate
    def test_delete_library_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "{protocol}://{ip}:{port}/library/sections/9683751588", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.delete_library(9683751588)
        responses.reset()

    @responses.activate
    def test_get_library_items(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/library/sections/6582958821/all",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_library_items(6582958821, 9, "quibusdam")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_library_items_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/library/sections/9837157577/all",
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
            "{protocol}://{ip}:{port}/library/sections/2390106765/all",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_library_items(2390106765, 1, "voluptas")
        responses.reset()

    @responses.activate
    def test_refresh_library(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/library/sections/6321566139/refresh",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.refresh_library(6321566139)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_refresh_library_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/library/sections/1404494475/refresh",
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
            "{protocol}://{ip}:{port}/library/sections/5664562376/refresh",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.refresh_library(5664562376)
        responses.reset()

    @responses.activate
    def test_get_latest_library_items(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/library/sections/7193296778/latest",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_latest_library_items(3, 7193296778, "optio")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_latest_library_items_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/library/sections/6458970563/latest",
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
            "{protocol}://{ip}:{port}/library/sections/1032189612/latest",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_latest_library_items(9, 1032189612, "enim")
        responses.reset()

    @responses.activate
    def test_get_common_library_items(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/library/sections/8358490584/common",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_common_library_items(7, 8358490584, "sed")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_common_library_items_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/library/sections/6763505882/common",
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
            "{protocol}://{ip}:{port}/library/sections/8191586203/common",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_common_library_items(2, 8191586203, "nobis")
        responses.reset()

    @responses.activate
    def test_get_metadata(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/library/metadata/2", json={}, status=200
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_metadata(2)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_metadata_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/library/metadata/3", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Library("testkey")
            test_service.get_metadata()
        responses.reset(),

    @responses.activate
    def test_get_metadata_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/library/metadata/5", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_metadata(5)
        responses.reset()

    @responses.activate
    def test_get_metadata_children(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/library/metadata/4/children", json={}, status=200
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_metadata_children(4)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_metadata_children_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/library/metadata/2/children", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Library("testkey")
            test_service.get_metadata_children()
        responses.reset(),

    @responses.activate
    def test_get_metadata_children_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "{protocol}://{ip}:{port}/library/metadata/9/children", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_metadata_children(9)
        responses.reset()

    @responses.activate
    def test_get_on_deck(self):
        # Mock the API response
        responses.get("{protocol}://{ip}:{port}/library/onDeck", json={}, status=200)
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_on_deck()
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_on_deck_error_on_non_200(self):
        # Mock the API response
        responses.get("{protocol}://{ip}:{port}/library/onDeck", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_on_deck()
        responses.reset()


if __name__ == "__main__":
    unittest.main()
