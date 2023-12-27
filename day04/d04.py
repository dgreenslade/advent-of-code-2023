import os
import numpy as np


def parse_input(file: str) -> list:
    """
    """
    games = []
    with open(file) as f:
        for line in f:
            winners = [int(x) for x in line.split(':')[1].split('|')[0]
                       .split()]
            card_nums = [int(x) for x in line.split(':')[1].split('|')[1]
                         .split()]
            games.append((winners, card_nums))
    return games


def part_one(games: list) -> list:
    game_scores = []
    for game in games:
        matched = []
        for num in game[0]:
            if num in game[1]:
                matched.append(num)
        if len(matched) > 0:
            game_scores.append(int(2**(len(matched)-1)))
    return game_scores


def part_two(games):
    card_copies = np.array([1] * len(games))
    for idx, game in enumerate(games):
        game_multiplier = card_copies[idx]
        matched = []
        for num in game[0]:
            if num in game[1]:
                matched.append(num)
        card_copies[idx+1: idx+1+len(matched)] += game_multiplier
    return card_copies


def main():
    file = os.path.join(os.getcwd(), 'day04', 'input.txt')
    games = parse_input(file)

    p1 = part_one(games)

    print('### Part 1 ###')
    print(sum(p1))

    p2 = part_two(games)

    print('### Part 2 ###')
    print(sum(p2))


if __name__ == "__main__":
    main()
