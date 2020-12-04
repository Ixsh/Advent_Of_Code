import re

fields = {
    'byr': re.compile('^(19[2-9]\d|200[0-2])$'),
    'iyr': re.compile('^(201\d|2020)$'),
    'eyr': re.compile('^(202\d|2030)$'),
    'hgt': re.compile('^(59in|6\din|7[0-6]in|1[5-8]\dcm|19[0-3]cm)$'),
    'hcl': re.compile('^#[0-9a-f]{6}$'),
    'ecl': re.compile('^(amb|blu|brn|gry|grn|hzl|oth)$'),
    'pid': re.compile('^[0-9]{9}$'),
    'cid': ''}


passports = []
with open('C:/Users/durha/Desktop/passports.txt', 'r') as f:
    passports = f.read().split('\n\n')

f.close()

def count_valid_passports(passports, ignore = []):
    count = 0
    checkedFields = list(set(fields.keys()) - set(ignore))
    for passport in passports:
        passport = passport.replace('\n', ' ')
        if all(field in passport for field in checkedFields):
            data = dict(x.split(':') for x in passport.split(' '))
            increment = True
            for key, value in data.items():
                if key not in checkedFields:
                    continue
                if not fields.get(key).match(value):
                    increment = False
                    break
            if increment:
                count += 1
    return count
                
print(count_valid_passports(passports, ['cid']))
