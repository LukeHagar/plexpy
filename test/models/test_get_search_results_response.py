import unittest
from src.plexsdk.models.GetSearchResultsResponse import GetSearchResultsResponse


class TestGetSearchResultsResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_search_results_response(self):
        # Create GetSearchResultsResponse class instance
        test_model = GetSearchResultsResponse(MediaContainer={"cum": 6})
        self.assertEqual(test_model.MediaContainer, {"cum": 6})


if __name__ == "__main__":
    unittest.main()
