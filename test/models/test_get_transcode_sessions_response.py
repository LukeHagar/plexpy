import unittest
from src.plexsdk.models.GetTranscodeSessionsResponse import GetTranscodeSessionsResponse


class TestGetTranscodeSessionsResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_transcode_sessions_response(self):
        # Create GetTranscodeSessionsResponse class instance
        test_model = GetTranscodeSessionsResponse(MediaContainer={"eaque": 9})
        self.assertEqual(test_model.MediaContainer, {"eaque": 9})


if __name__ == "__main__":
    unittest.main()
