# write a python program to get a password from a user and make
# sure that password should contain number and alphabets
import string
import random

# alphabets = alphabets = list(string.ascii_letters)
# numbers = list(range(0, 10))

user_input = input('Enter your password here: ')
if(user_input.isalnum()):
    print('Correct Password')
else:
    print('Incorrect password')
