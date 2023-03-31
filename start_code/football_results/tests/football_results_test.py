import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    
    def setUp(self):
        self.final_score = [{
            "home_score" : 3,
            "away_score" : 1
        },
        {
            "home_score" : 0,
            "away_score" : 1
        },
        {
            "home_score" : 2,
            "away_score" : 2
        }]

    # Test we get the right result string for a final score dictionary representing -
    def test_get_result_home_win(self):
        actual_result = get_result(self.final_score[0])
        expected_result = "Home win"
        self.assertEqual(expected_result, actual_result)

    def test_get_result_away_win(self):
        actual_result = get_result(self.final_score[1])
        expected_result = "Away win"
        self.assertEqual(expected_result, actual_result)

    def test_get_result_draw(self):
        actual_result = get_result(self.final_score[2])
        expected_result = "Draw"
        self.assertEqual(expected_result, actual_result)

    # Test we get right list of result strings for a list of final score dictionaries. 
    def test_can_get_list_of_results(self):
        actual_result = get_results(self.final_score)
        expected_result = ["Home win", "Away win", "Draw"]
        self.assertEqual(expected_result, actual_result)

if __name__ == "__main__":
    unittest.main()
