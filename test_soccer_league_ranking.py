import unittest
from io import StringIO
from unittest.mock import patch
from soccer_league_ranking import parse_game_result, calculate_points, process_results, format_output, main

class TestSoccerLeagueRanking(unittest.TestCase):
    def test_parse_game_result(self):
        self.assertEqual(parse_game_result("Lions 3, Snakes 3"), ("Lions", "Snakes", 3, 3))
        self.assertEqual(parse_game_result("Tarantulas 1, FC Awesome 0"), ("Tarantulas", "FC Awesome", 1, 0))
        with self.assertRaises(ValueError):
            parse_game_result("Invalid Input")

    def test_calculate_points(self):
        self.assertEqual(calculate_points(3, 3), (1, 1))
        self.assertEqual(calculate_points(1, 0), (3, 0))
        self.assertEqual(calculate_points(0, 1), (0, 3))

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

    def test_format_output(self):
        rankings = [
            ("Tarantulas", 6),
            ("Lions", 5),
            ("FC Awesome", 1),
            ("Snakes", 1),
            ("Grouches", 0)
        ]
        expected_output = (
            "1. Tarantulas, 6 pts\n"
            "2. Lions, 5 pts\n"
            "3. FC Awesome, 1 pt\n"
            "3. Snakes, 1 pt\n"
            "5. Grouches, 0 pts"
        )
        self.assertEqual(format_output(rankings), expected_output)

    @patch('sys.stdin', new_callable=StringIO)
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_function(self, mock_stdout, mock_stdin):
        mock_stdin.write("Lions 3, Snakes 3\n")
        mock_stdin.write("Tarantulas 1, FC Awesome 0\n")
        mock_stdin.write("Lions 1, FC Awesome 1\n")
        mock_stdin.write("Tarantulas 3, Snakes 1\n")
        mock_stdin.write("Lions 4, Grouches 0\n")
        mock_stdin.seek(0)
        
        main()
        
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