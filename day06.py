def solve_first(data):
    groups = list()
    group = set()
    for line in data:
        if line == '\n':
            groups.append(group)
            group = set()
        for c in line.rstrip():
            group.add(c)
    else:
        groups.append(group)
    total = sum((len(g) for g in groups))
    print(total)

def solve_second(data):
    groups = list()
    group = set()
    is_first_in_group = True
    for line in data:
        answer = set()
        if line == '\n':
            groups.append(group)
            group = set()
            is_first_in_group = True
        else:
            for c in line.rstrip():
                if is_first_in_group:
                    group.add(c)
                else:
                    answer.add(c)
            if not is_first_in_group:
                group = group.intersection(answer)
            is_first_in_group = False
    else:
        groups.append(group)
    total = sum((len(g) for g in groups))
    print(total)

with open('./inputs/day06') as data:
    solve_first(data)
    data.seek(0)
    solve_second(data)
