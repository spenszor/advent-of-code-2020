import re
def solve_first(passports):
    mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid = 0
    for p in passports:
        if all(f in p for f in mandatory_fields):
            valid += 1
    print(valid)

def is_valid(p):
    return (1920 <= int(p['byr']) <= 2002
            and 2010 <= int(p['iyr']) <= 2020
            and 2020 <= int(p['eyr']) <= 2030
            and ((hgt := p['hgt']).endswith('cm')
                    and 150 <= int(hgt[:-2]) <= 193
                    or hgt.endswith('in') and 59 <= int(hgt[:-2]) <= 76)
            and len(hcl := p['hcl']) == 7 and hcl[0] == '#'
            and all(c in '0123456789abcdef' for c in hcl[1:])
            and p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and len(pid := p['pid']) == 9
            and all(c in '0123456789' for c in pid))

def solve_second(raw_passports):
    mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passports = list()
    for p in raw_passports:
        if all(f in p for f in mandatory_fields):
            passport_fields = list(map(lambda f: f.split(":"), p.split()))
            passport = dict()
            for k, v in passport_fields:
                passport[k] = v
            passports.append(passport)
    
    print(sum(map(is_valid, passports)))


with open('./inputs/day04') as data:
    passports = list()
    raw_passport = ""
    for line in data:
        if line == "\n":
            passports.append(raw_passport.lstrip())
            raw_passport = ""
        else:
            raw_passport += " " + line.rstrip()
    else:
        passports.append(raw_passport.lstrip())

    solve_first(passports)
    solve_second(passports)