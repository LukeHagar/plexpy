import unittest
from src.plexsdk.models.GetDevicesResponse import GetDevicesResponse


class TestGetDevicesResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_devices_response(self):
        # Create GetDevicesResponse class instance
        test_model = GetDevicesResponse(MediaContainer={"dolores": 3})
        self.assertEqual(test_model.MediaContainer, {"dolores": 3})


if __name__ == "__main__":
    unittest.main()
