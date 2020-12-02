def solve_first(policies):
    # oneliner
    #(sum(1 for (min, max, letter, password) in policies if (count := password.count(letter)) >= min and count <= max))
    counter = 0
    for (min, max, letter, password) in policies:
        count = password.count(letter)
        if count >= min and count <= max:
            counter += 1
    return counter

def solve_second(policies):
    # oneliner
    #sum(1 for (pos1, pos2, letter, pw) in policies if (pw[pos1 - 1] == letter) ^ (pw[pos2 - 1] == letter))
    counter = 0
    for (pos1, pos2, letter, password) in policies:
        letter1_correct = password[pos1 - 1] == letter
        letter2_correct = password[pos2 - 1] == letter
        if letter1_correct ^ letter2_correct:
            counter += 1
    return counter



with open('./inputs/day02') as data:
    policies = list()
    for line in data:
        split = line.split(" ")
        [min, max] = split[0].split("-")
        letter = split[1][0]
        password = split[2].rstrip()
        policies.append((int(min), int(max), letter, password))
    print(solve_first(policies))
    print(solve_second(policies))