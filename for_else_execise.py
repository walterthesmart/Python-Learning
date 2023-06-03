height = (input("Enter the list of heights separated by comma: "))
list = height.split(",")
print(list)
for i in range(len(list)):
    list[i] = int(list[i])


sum = 0
for person in list:
    sum = sum + person
print(sum)
average = sum/len(list)
print(average)



#for i in range(len(list) + 1):
#23, 78, 50, 67, 90, 99, 345, 78, 200, 70, 34