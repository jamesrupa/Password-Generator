import random
import hashlib

def menu():
    print('''
                                                   __
    ____  ____ ____________      ______  _________/ /
   / __ \/ __ `/ ___/ ___/ | /| / / __ \/ ___/ __  / 
  / /_/ / /_/ (__  |__  )| |/ |/ / /_/ / /  / /_/ /  
 / .___/\__,_/____/____/ |__/|__/\______/   \__,_/   
/_/____ ____  ____  ___  _________ _/ /_____  _____  
  / __ `/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/  
 / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /      
 \__, /\___/_/ /_/\___/_/   \__,_/\__/\____/_/       
/____/                                               
                                   
 ________________________________________________
/_____/_____/_____/_____/_____/_____/_____/_____/

    1   -   Password Picker
    2   -   MD5 Hasher
    ''')

    usr_input = int(input('Menu choice: '))
    if usr_input == 1:
        password()
    if usr_input == 2:
        md5hash()
    elif usr_input < 1 or usr_input > 2:
        print('Invalid choice!')
        menu()

def password():
    sym = input('Would u like to include symbols: ').lower().replace(" ", "")
    num = input('Would u like to use numbers: ').lower().replace(" ", "")
    cap = input('Would u like to use capital letters: ').lower().replace(" ", "")
    length = int(input('Enter length of password: '))

    pass_char = 'abcdefghijklmnopqrstuvwxyz'

    if sym == 'yes':
        pass_char += '!@#$%^&*()?'
    if num == 'yes':
        pass_char += '01234567890'
    if cap == 'yes':
        pass_char += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    password =  ''.join(random.sample(pass_char, length))
    print (f'Your {length} digit password is: {password}')

def md5hash():

    pre_hash = input('Enter what you want to hash: ')
    post_hash = hashlib.md5(pre_hash.encode())

    print("Your MD5 hash is: ", end ="") 
    print(post_hash.hexdigest()) 


menu()