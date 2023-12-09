import unittest
from src.plexsdk.models.GetServerIdentityResponse import GetServerIdentityResponse


class TestGetServerIdentityResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_server_identity_response(self):
        # Create GetServerIdentityResponse class instance
        test_model = GetServerIdentityResponse(MediaContainer={"eum": 5})
        self.assertEqual(test_model.MediaContainer, {"eum": 5})


if __name__ == "__main__":
    unittest.main()
