#write a program a program to get 2 numbers from user and display maximum number
import numpy

numbers = input('Enter two numbers separated by comma: ')
numbers = numbers.split(',')
digit = []
for num in numbers:
    digit.append(int(num))

maximum = max(digit)
print(digit)
print(maximum)