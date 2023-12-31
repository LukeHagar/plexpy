import unittest
from src.plexsdk.models.GetMyPlexAccountResponse import GetMyPlexAccountResponse


class TestGetMyPlexAccountResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_my_plex_account_response(self):
        # Create GetMyPlexAccountResponse class instance
        test_model = GetMyPlexAccountResponse(MyPlex={"at": 7})
        self.assertEqual(test_model.MyPlex, {"at": 7})


if __name__ == "__main__":
    unittest.main()
