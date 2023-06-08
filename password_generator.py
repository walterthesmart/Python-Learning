import string
import random
alphabets = list(string.ascii_letters)
symbols = list(string.punctuation)
numbers = list(range(0, 10))
print("Welcome to Password Generator!")
number_letters = int(input("How many letters would you like in your password?: \n"))
number_symbols = int(input("HOw many symbols would you like? "))
numbers = int(input("How many numbers would you like? "))
password = ""
for i in range(1, number_letters + 1):
    char = random.choice(alphabets)
    password += char
for i in range(1, number_symbols + 1):
    symb = random.choice(symbols)
    password += symb
for i in range(1, numbers + 1):
    numb = random.choice(numbers)
    password += numb
print(numbers)