#write a program to get 6 numbers in a list and display
#all numbers then clear list then display
numbers = input('Enter your numbers sepaarated by commas: ') #65,75,78,77,87,97
numbers = numbers.split(',')
lst = []
for i in numbers:
    lst.append(int(i))
print(lst)
lst.clear()
print('We have removed the list items')
print(lst)