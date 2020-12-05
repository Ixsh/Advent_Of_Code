# Open the file of numbers to check
with open('C:/Users/durha/Desktop/input.txt', 'r', encoding='utf-8') as f:
  arr = f.read().splitlines()

f.close()

def count_valid_passwords(passwords):
    count = 0
    for password in passwords:
        password  = password.split(' ')
        if len(password) == 3:
            i,j = map(int, password[0].split('-'))
            char = password[1].split(':')
            if (
                    password[2][i-1] == char[0] and
                    password[2][j-1] != char[0] or
                    password[2][i-1] != char[0] and
                    password[2][j-1] == char[0]
                ):
                count += 1
    return count

print(count_valid_passwords(arr))
