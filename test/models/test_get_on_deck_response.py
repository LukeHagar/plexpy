import unittest
from src.plexsdk.models.GetOnDeckResponse import GetOnDeckResponse


class TestGetOnDeckResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_on_deck_response(self):
        # Create GetOnDeckResponse class instance
        test_model = GetOnDeckResponse(MediaContainer={"sapiente": 6})
        self.assertEqual(test_model.MediaContainer, {"sapiente": 6})


if __name__ == "__main__":
    unittest.main()
