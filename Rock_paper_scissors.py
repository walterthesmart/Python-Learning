import random

computer = ["rock", "paper", "scissors"]
computer_choice = random.choice(computer)
user = str(input("Enter your choice:"))
print("COmputer chose")
print(computer_choice)

if user == computer_choice:
    print("It's a tie")
elif user == "rock" and computer_choice == "paper":
    print("Computer wins")
elif user == "rock" and computer_choice == "scissors":
    print("User wins")
elif user == "paper" and computer_choice == "rock":
    print("User wins")
elif user == "paper" and computer_choice == "scissors":
    print("Computer wins")
elif user == "scissors" and computer_choice == "rock":
    print("Computer wins")
else:
    print("Computer wins")