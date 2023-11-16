import unittest
from src.plexsdk.models.GetServerActivitiesResponse import GetServerActivitiesResponse


class TestGetServerActivitiesResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_server_activities_response(self):
        # Create GetServerActivitiesResponse class instance
        test_model = GetServerActivitiesResponse(MediaContainer={"sed": 7})
        self.assertEqual(test_model.MediaContainer, {"sed": 7})


if __name__ == "__main__":
    unittest.main()
