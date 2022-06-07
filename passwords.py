import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

n = int(input('Enter the number of passwords to generate: '))
length = int(input('Enter password length: '))
add_digit = input('Numbers include? (y = yes, n = no) ').strip()
add_lowercase = input('Enable uppercase letters? (y = yes, n = no) ').strip()
add_uppercase = input('Enable lowercase letters? (y = yes, n = no) ').strip()
add_punctuation = input('Include characters like !#$%&*+-=?@^_? (y = yes, n = no) ').strip()
remove_badsymbols = input('Exclude symbols il1Lo0O? (y = yes, n = no) ').strip()

if add_digit.lower() == 'y':
    chars += digits
if add_lowercase.lower() == 'y':
    chars += lowercase_letters
if add_uppercase.lower() == 'y':
    chars += uppercase_letters
if add_punctuation.lower() == 'y':
    chars += punctuation
if remove_badsymbols.lower() == 'y':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    print(password)


for _ in range(n):
    generate_password(length, chars)














