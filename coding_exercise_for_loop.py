numbers = input("Enter list of numbers separated by commas: ")
# 49,46, 48, 90, 74, 467, 283, 78

numbers = numbers.split(",")
count = 0
for number in numbers:
    count = count + 1
print(f"The lenght of the list is : {count}")
for i in range(count):
    numbers[i] = int(numbers[i])
maximum_number = numbers[0]
for number in numbers:
    if number > maximum_number:
        maximum_number = number
print(f"The maximum number is : {maximum_number}")