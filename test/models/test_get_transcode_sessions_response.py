import unittest
from src.plexsdk.models.GetTranscodeSessionsResponse import GetTranscodeSessionsResponse


class TestGetTranscodeSessionsResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_transcode_sessions_response(self):
        # Create GetTranscodeSessionsResponse class instance
        test_model = GetTranscodeSessionsResponse(MediaContainer={"fugit": 8})
        self.assertEqual(test_model.MediaContainer, {"fugit": 8})


if __name__ == "__main__":
    unittest.main()
