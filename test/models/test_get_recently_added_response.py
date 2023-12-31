import unittest
from src.plexsdk.models.GetRecentlyAddedResponse import GetRecentlyAddedResponse


class TestGetRecentlyAddedResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_recently_added_response(self):
        # Create GetRecentlyAddedResponse class instance
        test_model = GetRecentlyAddedResponse(MediaContainer={"possimus": 4})
        self.assertEqual(test_model.MediaContainer, {"possimus": 4})


if __name__ == "__main__":
    unittest.main()
