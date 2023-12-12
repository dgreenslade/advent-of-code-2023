import sys
import pathlib
import os
import re


def parse_game(game_info: str) -> list:
    game = []
    for draw in game_info.split(';'):
        draw_result = {'red': 0, 'green': 0, 'blue': 0}
        for colour in draw_result:
            num = re.search(rf'\d+(?=\s{colour})', draw)
            draw_result.update({colour: int(num[0]) if num else 0})
        game.append(draw_result)
    return game


def parse_input(file: str) -> list:
    results = []
    with open(file) as f:
        for line in f:
            game = {
                'game_num': int(re.search(r'\d+', line.split(':')[0])[0]),
                'draws': parse_game(line.split(':')[1])
            }
            results.append(game)
    return results


def game_maximum(draws: list) -> dict:
    """
    Take list of draws from a single game result
    and return a dict of maximum scores for each colour
    """
    maximum = {'red': 0, 'green': 0, 'blue': 0}
    for draw in draws:
        for colour in draw:
            if draw[colour] > maximum[colour]:
                maximum[colour] = draw[colour]
    return maximum


def all_maximums(games: list) -> list:
    """
    Take original list of games and return new list with
    'maxes' of maximum game scores rather than list of draws
    """
    all_maxes = []
    for game in games:
        max = {
            'game_num': game['game_num'],
            'maxes': game_maximum(game['draws'])
        }
        all_maxes.append(max)
    return all_maxes


def part_one(games):
    needed_max = {'red': 12, 'green': 13, 'blue': 14}
    invalid = set()
    for game in games:
        for colour in needed_max:
            if game['maxes'][colour] > needed_max[colour]:
                invalid.add(game['game_num'])
    all = set([game['game_num'] for game in games])
    valid = all - invalid
    return sum(valid)


def part_two(games):
    scores = []
    for game in games:
        game_score = 1
        for colour in game['maxes']:
            game_score *= game['maxes'][colour]
        scores.append(game_score)
    return sum(scores)


def main():

    file = os.path.join(pathlib.Path(__file__).parent.resolve(), sys.argv[1])
    input = parse_input(file)
    print('   ### Input ###')
    print(input[:3])

    print('   ### All Maxes ###')
    all_maxes = all_maximums(input)
    print(all_maxes[:3])

    print('   ### Part 1 ###')
    print(part_one(all_maxes))

    print('   ### Part 2 ###')
    print(part_two(all_maxes))


if __name__ == "__main__":
    main()
