import operator as op
from functools import reduce


def countTeams(skills, minPlayers, minLevel, maxLevel):
    player_counter = 0
    for player in skills:
        if minLevel <= player <= maxLevel:
            player_counter += 1

    if player_counter < minPlayers:
        return 0

    answer = 0
    for min_player in range(minPlayers, player_counter + 1):
        answer += nCr(player_counter, min_player)

    return answer


def nCr(n, r):
    if n < 1 or r < 0 or n < r:
        raise ValueError
    r = min(r, n - r)
    numerator = reduce(op.mul, range(n, n - r, -1), 1)
    denominator = reduce(op.mul, range(1, r + 1), 1)
    return numerator // denominator


def test_solution():
    assert countTeams([12, 4, 6, 13, 5, 10], 3, 4, 10) == 5
