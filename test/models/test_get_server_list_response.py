import unittest
from src.plexsdk.models.GetServerListResponse import GetServerListResponse


class TestGetServerListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_server_list_response(self):
        # Create GetServerListResponse class instance
        test_model = GetServerListResponse(MediaContainer={"sequi": 9})
        self.assertEqual(test_model.MediaContainer, {"sequi": 9})


if __name__ == "__main__":
    unittest.main()
