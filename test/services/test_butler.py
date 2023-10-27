import unittest
import responses
from src.plexsdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.plexsdk.services.butler import Butler


class TestButler_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_butler_tasks(self):
        # Mock the API response
        responses.get("{protocol}://{ip}:{port}/butler", json={}, status=200)
        # call the method to test
        test_service = Butler("testkey")
        response = test_service.get_butler_tasks()
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_butler_tasks_error_on_non_200(self):
        # Mock the API response
        responses.get("{protocol}://{ip}:{port}/butler", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Butler("testkey")
            test_service.get_butler_tasks()
        responses.reset()

    @responses.activate
    def test_start_all_tasks(self):
        # Mock the API response
        responses.post("{protocol}://{ip}:{port}/butler", json={}, status=200)
        # call the method to test
        test_service = Butler("testkey")
        response = test_service.start_all_tasks()
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_start_all_tasks_error_on_non_200(self):
        # Mock the API response
        responses.post("{protocol}://{ip}:{port}/butler", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Butler("testkey")
            test_service.start_all_tasks()
        responses.reset()

    @responses.activate
    def test_stop_all_tasks(self):
        # Mock the API response
        responses.delete("{protocol}://{ip}:{port}/butler", json={}, status=200)
        # call the method to test
        test_service = Butler("testkey")
        response = test_service.stop_all_tasks()
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_stop_all_tasks_error_on_non_200(self):
        # Mock the API response
        responses.delete("{protocol}://{ip}:{port}/butler", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Butler("testkey")
            test_service.stop_all_tasks()
        responses.reset()

    @responses.activate
    def test_start_task(self):
        # Mock the API response
        responses.post(
            "{protocol}://{ip}:{port}/butler/BackupDatabase", json={}, status=200
        )
        # call the method to test
        test_service = Butler("testkey")
        response = test_service.start_task("BackupDatabase")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_start_task_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "{protocol}://{ip}:{port}/butler/BackupDatabase", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Butler("testkey")
            test_service.start_task()
        responses.reset(),

    @responses.activate
    def test_start_task_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "{protocol}://{ip}:{port}/butler/BackupDatabase", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Butler("testkey")
            test_service.start_task("BackupDatabase")
        responses.reset()

    @responses.activate
    def test_stop_task(self):
        # Mock the API response
        responses.delete(
            "{protocol}://{ip}:{port}/butler/BackupDatabase", json={}, status=200
        )
        # call the method to test
        test_service = Butler("testkey")
        response = test_service.stop_task("BackupDatabase")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_stop_task_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "{protocol}://{ip}:{port}/butler/BackupDatabase", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Butler("testkey")
            test_service.stop_task()
        responses.reset(),

    @responses.activate
    def test_stop_task_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "{protocol}://{ip}:{port}/butler/BackupDatabase", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Butler("testkey")
            test_service.stop_task("BackupDatabase")
        responses.reset()


if __name__ == "__main__":
    unittest.main()
