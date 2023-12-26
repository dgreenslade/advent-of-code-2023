import os
import numpy as np


def parse_input(file: str) -> list:
    """ Parse input file, return two lists:
    - list of symbos tuples
    (character, index of the input line string)
    - list of part numbers
    (number:int, index of the first digit of the inut string)
    """
    nums = []
    symbols = []
    with open(file) as f:
        for line in f:
            line_nums = []
            line_symbols = []
            line = line.rstrip()
            num = ''
            for idx, char in enumerate(line.rstrip()):
                if char.isdigit():
                    num += char
                elif char != '.':
                    line_symbols.append((char, idx))
                if (not char.isdigit() or len(line) == idx + 1) and num != '':
                    line_nums.append((int(num), idx - len(num)))
                    num = ''
            nums.append(line_nums)
            symbols.append(line_symbols)
    return nums, symbols


def part_one(nums: list, symbols: list) -> int:
    """ Compare symbol list locations to part num locations.
    Use length of part num digit to determine end index from string
    """
    found = []
    for idx, line in enumerate(symbols):
        for symbol in line:
            if len(symbol) > 0:
                for line2 in nums[idx-1: idx+2]:
                    for num in line2:
                        if symbol[1] - len(str(num[0])) <= num[1] <= symbol[1] + 1:
                            found.append((num[0]))
    return found


def part_two(nums: list, symbols: list) -> int:
    """ As part one but only process if symbol is an asterix."""
    gear_ratios = []
    for idx, line in enumerate(symbols):
        for symbol in line:
            if symbol[0] == '*':
                part_nums = []
                for line2 in nums[idx-1: idx+2]:
                    for num in line2:
                        if symbol[1] - len(str(num[0])) <= num[1] <= symbol[1] + 1:
                            part_nums.append(num[0])
                if len(part_nums) == 2:
                    gear_ratios.append(np.prod(part_nums))
    return gear_ratios


def main():

    file = os.path.join(os.getcwd(), 'day03', 'input.txt')
    nums, symbols = parse_input(file)
    print('   ### Input ###')

    print('### Part 1 ###')
    print(sum(part_one(nums, symbols)))

    print('### Part 2 ###')
    print(sum(part_two(nums, symbols)))


if __name__ == "__main__":
    main()
