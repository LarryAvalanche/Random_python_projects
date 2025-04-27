c , l , s , n = 0 , 0, 0, 0
password = input('Enter password : ')
cap_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
low_letters = 'abcdefghijklmnopqrstuvwxyz'
special_char = '!@#$%^&*()_+'
num = '1234567890'

if len(password) >= 15:
    for i in password:
        if i in cap_letters:
            c += 1
        if i in low_letters:
            l += 1
        if i in special_char:
            s += 1
        if i in num:
            n += 1

def check_func():
    if (c >= 1 and l >= 1 and s >= 1 and n >= 1
            and c + l + s + n == len(password)):
        print("Password Valid")
        return True

while not check_func():
    print("Password Invalid ! Try Again")
    password = input('Enter password : ')