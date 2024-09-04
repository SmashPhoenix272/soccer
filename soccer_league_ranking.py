import sys
import re
from collections import defaultdict
from typing import List, Tuple

def parse_game_result(line: str) -> Tuple[str, str, int, int]:
    pattern = r'^([\w\s]+) (\d+), ([\w\s]+) (\d+)$'
    match = re.match(pattern, line.strip())
    if match:
        team1, score1, team2, score2 = match.groups()
        return team1.strip(), team2.strip(), int(score1), int(score2)
    raise ValueError(f"Invalid input line: {line}")

def calculate_points(score1: int, score2: int) -> Tuple[int, int]:
    if score1 > score2:
        return 3, 0
    elif score1 < score2:
        return 0, 3
    else:
        return 1, 1

def process_results(lines: List[str]) -> List[Tuple[str, int]]:
    team_points = defaultdict(int)
    
    for line in lines:
        if line.strip():  # Skip empty lines
            try:
                team1, team2, score1, score2 = parse_game_result(line)
                points1, points2 = calculate_points(score1, score2)
                team_points[team1] += points1
                team_points[team2] += points2
            except ValueError:
                # Skip invalid lines
                continue
    
    return sorted(team_points.items(), key=lambda x: (-x[1], x[0]))

def format_output(rankings: List[Tuple[str, int]]) -> str:
    output = []
    for i, (team, points) in enumerate(rankings, start=1):
        if i > 1 and points == rankings[i-2][1]:
            rank = output[-1].split('.')[0]
        else:
            rank = str(i)
        
        point_str = 'pt' if points == 1 else 'pts'
        output.append(f"{rank}. {team}, {points} {point_str}")
    
    return "\n".join(output)

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()
    
    if not lines:
        print("No input provided.")
        return

    rankings = process_results(lines)
    print(format_output(rankings))

if __name__ == "__main__":
    main()