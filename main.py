import random

print('this is a password generator')
print('would u like to include symbols')
print('would u like to use numbers')
print('would u like to use capital letters')
len = int(input('enter length of password: '))

# TODO: add logic if statements for different types of passwords

pass_char = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
password =  ''.join(random.sample(pass_char, len ))
print(password)