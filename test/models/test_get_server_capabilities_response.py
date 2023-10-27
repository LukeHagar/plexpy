import unittest
from src.plexsdk.models.GetServerCapabilitiesResponse import (
    GetServerCapabilitiesResponse,
)


class TestGetServerCapabilitiesResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_server_capabilities_response(self):
        # Create GetServerCapabilitiesResponse class instance
        test_model = GetServerCapabilitiesResponse(MediaContainer={"nam": 5})
        self.assertEqual(test_model.MediaContainer, {"nam": 5})


if __name__ == "__main__":
    unittest.main()
