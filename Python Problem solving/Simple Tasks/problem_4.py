#write a program to take age fro user to check if user is able to participate in voting or not.
#If age is less than 18 then will not allow particpaton
age = int(input('Enter your age: '))
years_left = 18 - age
if age < 18:
    print(f'Sorry! You cannot participate in voting, you will be able to participate after {years_left} years')
else:
    print('Carry on with the voting')