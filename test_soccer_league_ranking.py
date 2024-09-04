import unittest
from io import StringIO
from unittest.mock import patch
from soccer_league_ranking import process_results, main

class TestSoccerLeagueRanking(unittest.TestCase):
    def test_process_results(self):
        input_lines = [
            "Lions 3, Snakes 3",
            "Tarantulas 1, FC Awesome 0",
            "Lions 1, FC Awesome 1",
            "Tarantulas 3, Snakes 1",
            "Lions 4, Grouches 0"
        ]
        expected_output = [
            ("Tarantulas", 6),
            ("Lions", 5),
            ("FC Awesome", 1),
            ("Snakes", 1),
            ("Grouches", 0)
        ]
        self.assertEqual(process_results(input_lines), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_function(self, mock_stdout):
        input_lines = [
            "Lions 3, Snakes 3",
            "Tarantulas 1, FC Awesome 0",
            "Lions 1, FC Awesome 1",
            "Tarantulas 3, Snakes 1",
            "Lions 4, Grouches 0"
        ]
        
        main(input_lines)
        
        expected_output = (
            "1. Tarantulas, 6 pts\n"
            "2. Lions, 5 pts\n"
            "3. FC Awesome, 1 pt\n"
            "3. Snakes, 1 pt\n"
            "5. Grouches, 0 pts\n"
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()