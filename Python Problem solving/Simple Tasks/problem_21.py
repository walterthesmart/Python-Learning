#write a program to get 5 number from user in array, find the max number
import array as arr
numbers = input('Enter 5 numbers: ')
numbers = numbers.split(',')
a = arr.array('b',[])
for i in  numbers:
    a.append(int(i))
for j in a:
    print(a[j])
#print(a)