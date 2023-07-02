#write a program to het 5 num from user and store in array
#sum all number and display
import array as arr
numbers = input('Enter 3 numbers: ')
numbers = numbers.split(',')
a = arr.array('i', [])

for i in numbers:
    a.append(int(i))
for j in a:
    print(a[j])
