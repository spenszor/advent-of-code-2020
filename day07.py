import re

def verify_bags(color, rules):
    bags = rules[color]
    has_gold = any(clr == 'shiny gold' for _, clr in bags)
    return has_gold or any(verify_bags(clr, rules) for _, clr in bags)

def count_bags(color, rules):
    bags = rules[color]
    return sum(am for am, _ in bags) + sum(am * count_bags(clr, rules) for am, clr in bags)

with open('./inputs/day07') as data:
    rules = dict()
    pattern_main = r'(.*) bags contain (.*)'
    pattern_sub = r'.*(\d) (.*) bag'

    for l in data:
        match = re.search(pattern_main, l.rstrip())
        bag_color = match.groups()[0]
        raw_rules = match.groups()[1].split(',')
        for rr in raw_rules:
            if bag_color not in rules:
                rules[bag_color] = list()
            rule = re.match(pattern_sub, rr)
            if rule:
                amount = rule.groups()[0]
                color = rule.groups()[1]
                rules[bag_color].append((int(amount), color))

    print(sum(1 for color in rules.keys() if verify_bags(color, rules)))
    print(count_bags('shiny gold', rules))