# Simulate a sports tournament

import csv
import sys
import random
import time

# Number of simulations to run
N = [10, 100, 1000, 10000, 100000, 1000000]


def main():
    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    # TODO: Read teams into memory from file
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Store each team as a dictionary in a list of teams
            # rating is a string, convert to integer
            name = row["team"]
            rating = int(row["rating"])
            teams.append({"team": name, "rating": rating})

    count = 10
    for n in N:
        # Start timer
        start = time.time()
        counts = {}
        # TODO: Simulate N tournaments and keep track of win counts
        # Runs N times
        for i in range(n):
            # simulate_tournament() returns name of tournament winner
            winner = simulate_tournament(teams)
            # If winner has won before, add 1 to wins tally
            if winner in counts:
                counts[winner] += 1
            # Otherwise this is winner's first win
            else:
                counts[winner] = 1

        runtime = time.time() - start
        # Print each team's chances of winning, according to simulation
        for team in sorted(counts, key=lambda team: counts[team], reverse=True):
            print(f"{team}: {counts[team] * 100 / n:.1f}% chance of winning")

        print(f"Run time ({count}): {runtime: .3f}s")
        count = count * 10


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO
    while len(teams) > 1:
        teams = simulate_round(teams)

    return teams[0]["team"]


if __name__ == "__main__":
    main()