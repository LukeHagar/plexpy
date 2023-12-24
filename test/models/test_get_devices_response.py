import unittest
from src.plexsdk.models.GetDevicesResponse import GetDevicesResponse


class TestGetDevicesResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_devices_response(self):
        # Create GetDevicesResponse class instance
        test_model = GetDevicesResponse(MediaContainer={"autem": 2})
        self.assertEqual(test_model.MediaContainer, {"autem": 2})


if __name__ == "__main__":
    unittest.main()
