from itertools import combinations


def solve_first(data):
    for a, b in combinations(data, 2):
        if a + b == 2020:
            return a * b


def solve_second(data):
    for a, b, c in combinations(data, 3):
        if a + b + c == 2020:
            return a * b * c


with open('./inputs/day01') as data:
    parsed = [int(x) for x in data]
    print(f'First solution: {solve_first(parsed)}')
    print(f'Second solution: {solve_second(parsed)}')
