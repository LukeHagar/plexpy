import unittest
from src.plexsdk.models.GetTranscodeSessionsResponse import GetTranscodeSessionsResponse


class TestGetTranscodeSessionsResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_transcode_sessions_response(self):
        # Create GetTranscodeSessionsResponse class instance
        test_model = GetTranscodeSessionsResponse(MediaContainer={"ab": 3})
        self.assertEqual(test_model.MediaContainer, {"ab": 3})


if __name__ == "__main__":
    unittest.main()
