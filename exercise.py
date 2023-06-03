import random

a = input("Enter everybody's name separated by comma:")

names = a.split(",")

x = random.choice(names)

print(str(x) + " will have to pay for everybody's bill")
