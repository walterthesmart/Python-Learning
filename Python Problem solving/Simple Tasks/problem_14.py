#write a program to get 6 number from the user
#and store number in a list then sum them up
numbers = input('Enter your numbers sepaarated by commas: ')
numbers = numbers.split(',')
list = []
for i in numbers:
    list.append(int(i))
total = 0
for num in list:
    total += num
print(total)