import random

print('this is a password generator')
sym = input('would u like to include symbols: ').lower().replace(" ", "")
num = input('would u like to use numbers: ').lower().replace(" ", "")
cap = input('would u like to use capital letters: ').lower().replace(" ", "")
len = int(input('enter length of password: '))

pass_char = 'abcdefghijklmnopqrstuvwxyz'

if sym == 'yes':
    pass_char += '!@#$%^&*()?'
if num == 'yes':
    pass_char += '01234567890'
if cap == 'yes':
    pass_char += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

password =  ''.join(random.sample(pass_char, len ))
print(password)