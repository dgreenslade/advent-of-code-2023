import re
import sys
import pathlib
import os


def parse_input(file: str) -> list:
    with open(file) as f:
        input = [line.rstrip() for line in f]
    return input


def bookend_ints(input: list, replace_words=False) -> list:
    """
    Return list of leftmost & rightmost single digit integers
    concatenated into two digit integer.
    """
    ints = []
    for line in input:
        # Part 1git 
        if replace_words is False:
            found = re.findall(r'\d', line)
        # Part 2
        elif replace_words:
            found = digit_or_word_bookends(line)
        if len(found) > 0:
            ints.append(int(found[0] + found[-1]))
    return ints


def digit_or_word_bookends(line: str) -> str:
    """
    Search for integers or word representations of them.
    Only returns rightmost & leftmost, as a tuple of found
    & translated integers (as strings)
    """
    translate = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
    }
    search_pattern = '|'.join(list(translate) + list(translate.values()))
    # Search from both left then right (by reversing match pattern & string)
    left = re.search(search_pattern, line).group()
    right = re.search(search_pattern[::-1], line[::-1]).group()[::-1]
    for word, integer in translate.items():
        left = left.replace(word, integer)
        right = right.replace(word, integer)
    return left, right


def main():

    file = os.path.join(pathlib.Path(__file__).parent.resolve(), sys.argv[1])
    input = parse_input(file)

    # # Part 1
    int_list = bookend_ints(input)
    # print(int_list)
    print(f'Part 1 sum is: {sum(int_list)}')

    # # Part 2
    int_list = bookend_ints(input, replace_words=True)
    # print(int_list)
    print(f'Part 2 sum is: {sum(int_list)}')


if __name__ == "__main__":
    main()