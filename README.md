# Soccer League Ranking

This is a command-line application that calculates the ranking table for a soccer league.

## Requirements

- Python 3.6 or higher

## Installation

No additional libraries are required. Simply clone or download this repository to your local machine.

## Usage

### Running the application

You can run the application in two ways:

1. Providing input via stdin:
   ```
   python soccer_league_ranking.py < sample-input.txt
   ```

2. Providing input file as a command-line argument:
   ```
   python soccer_league_ranking.py sample-input.txt
   ```

### Running the tests

To run the tests, use the following command:

```
python -m unittest test_soccer_league_ranking.py
```

## Input Format

The input should be a list of game results, one per line, in the following format:

```
Team1 Score1, Team2 Score2
```

For example:
```
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0
```

## Output Format

The output will be a ranking table, sorted from most to least points, in the following format:

```
1. Team1, X pts
2. Team2, Y pts
3. Team3, Z pts
...
```

Teams with the same number of points are ranked in alphabetical order and share the same rank number.

## Rules

- A win is worth 3 points
- A draw is worth 1 point
- A loss is worth 0 points