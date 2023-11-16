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
        response = test_service.get_file_hash("doloribus", 2)
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
            test_service.get_file_hash("aut", 9)
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
            "http://10.10.10.47:32400/library/sections/8820585836", json={}, status=200
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_library(8820585836, 9)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_library_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/6885092592", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Library("testkey")
            test_service.get_library()
        responses.reset(),

    @responses.activate
    def test_get_library_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/6716168527", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_library(6716168527, 4)
        responses.reset()

    @responses.activate
    def test_delete_library(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/library/sections/5130081697", json={}, status=200
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.delete_library(5130081697)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_delete_library_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/library/sections/7212508397", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Library("testkey")
            test_service.delete_library()
        responses.reset(),

    @responses.activate
    def test_delete_library_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "http://10.10.10.47:32400/library/sections/1942042738", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.delete_library(1942042738)
        responses.reset()

    @responses.activate
    def test_get_library_items(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/8012335957/all",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_library_items(8012335957, 8, "porro")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_library_items_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/6329608079/all",
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
            "http://10.10.10.47:32400/library/sections/7003632597/all",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_library_items(7003632597, 5, "magni")
        responses.reset()

    @responses.activate
    def test_refresh_library(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/4426359171/refresh",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.refresh_library(4426359171)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_refresh_library_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/5343440474/refresh",
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
            "http://10.10.10.47:32400/library/sections/5876897013/refresh",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.refresh_library(5876897013)
        responses.reset()

    @responses.activate
    def test_get_latest_library_items(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/5131694225/latest",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_latest_library_items(9, 5131694225, "non")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_latest_library_items_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/4058098584/latest",
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
            "http://10.10.10.47:32400/library/sections/4781224326/latest",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_latest_library_items(5, 4781224326, "iure")
        responses.reset()

    @responses.activate
    def test_get_common_library_items(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/9179339262/common",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_common_library_items(8, 9179339262, "fugiat")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_common_library_items_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/sections/9729167528/common",
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
            "http://10.10.10.47:32400/library/sections/2534656820/common",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_common_library_items(4, 2534656820, "ipsa")
        responses.reset()

    @responses.activate
    def test_get_metadata(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/metadata/2", json={}, status=200
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
            "http://10.10.10.47:32400/library/metadata/3", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Library("testkey")
            test_service.get_metadata()
        responses.reset(),

    @responses.activate
    def test_get_metadata_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/metadata/7", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Library("testkey")
            test_service.get_metadata(7)
        responses.reset()

    @responses.activate
    def test_get_metadata_children(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/metadata/9/children", json={}, status=200
        )
        # call the method to test
        test_service = Library("testkey")
        response = test_service.get_metadata_children(9)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_metadata_children_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/library/metadata/9/children", json={}, status=202
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
