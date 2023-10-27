import unittest
from src.plexsdk.models.GetOnDeckResponse import GetOnDeckResponse


class TestGetOnDeckResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_on_deck_response(self):
        # Create GetOnDeckResponse class instance
        test_model = GetOnDeckResponse(MediaContainer={"doloremque": 5})
        self.assertEqual(test_model.MediaContainer, {"doloremque": 5})


if __name__ == "__main__":
    unittest.main()
