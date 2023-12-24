import unittest
from src.plexsdk.models.GetServerActivitiesResponse import GetServerActivitiesResponse


class TestGetServerActivitiesResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_server_activities_response(self):
        # Create GetServerActivitiesResponse class instance
        test_model = GetServerActivitiesResponse(MediaContainer={"quisquam": 7})
        self.assertEqual(test_model.MediaContainer, {"quisquam": 7})


if __name__ == "__main__":
    unittest.main()
