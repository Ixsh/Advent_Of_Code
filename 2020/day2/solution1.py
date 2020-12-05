with open('input.txt', 'r', encoding='utf-8') as f:
  arr = f.read().splitlines()

f.close()

def count_valid_passwords(passwords):
    count = 0
    for password in passwords:
        password  = password.split(' ')
        if len(password) == 3:
            lower,upper = map(int, password[0].split('-'))
            char = password[1].split(':')
            if lower <= password[2].count(char[0]) <= upper:
                count += 1
    return count

print(count_valid_passwords(arr))
