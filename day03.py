def count_trees(slope, step, max_x, max_y):
    cur_x = 0
    cur_y = 0
    trees = 0
    while cur_y < max_y:
        cur_x = (cur_x + step[0]) % (max_x + 1) # max_x is still a position on a slope
        cur_y += step[1]
        current_pos = (cur_x, cur_y)
        if slope[current_pos] == '#':
            trees += 1
    return trees

with open('./inputs/day03') as data:
    slope = dict()
    y = 0
    for line in data:
        for x, ch in enumerate(line.rstrip()):
            slope[(x, y)] = ch
        y = y + 1
    (max_x, max_y) = max(slope.keys())
    # part 1
    print(count_trees(slope, (3, 1), max_x, max_y))
    # part 2
    steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    total = 1
    for step in steps:
        total *= count_trees(slope, step, max_x, max_y)
    print(total)
    


