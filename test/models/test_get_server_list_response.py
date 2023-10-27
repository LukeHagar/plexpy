import unittest
from src.plexsdk.models.GetServerListResponse import GetServerListResponse


class TestGetServerListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_server_list_response(self):
        # Create GetServerListResponse class instance
        test_model = GetServerListResponse(MediaContainer={"asperiores": 6})
        self.assertEqual(test_model.MediaContainer, {"asperiores": 6})


if __name__ == "__main__":
    unittest.main()
