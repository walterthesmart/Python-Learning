#write a program to get 3 numbers fro user and put
#in the following equation a+b+ca/b(2a+3b)

numbers = input('Enter 3 numbers: ')
numbers = numbers.split(',')
lst = []
for i in numbers:
    lst.append(int(i))
a = lst[0]
b = lst[1]
c = lst[2]
print(a+b+(c*a)/(b(2*a+3*b)))
print(a+b)