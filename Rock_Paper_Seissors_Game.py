# rock,paper,scissors game

import random

print("Welcome to Rock Paper Scissors game.")
choices = ["rock", "paper", "scissors"]

user = input("Enter your choice (Rock or Paper or Scissors): ")
computer  = random.choice(choices)

print("Computer:",computer)

# tie case
if user == computer:
    print(f"Both player choose same {user}.It's a tie.")

# user winning case
elif user =="rock" and computer == "scissors":
    print("User win.")
elif user == "paper" and computer == "rock":
    print("User win.")
elif user == "scissors" and computer == "paper":
    print("User win.")

# computer winning case
elif user =="scissors" and computer == "rock":
    print("Computer win.")
elif user == "rock" and computer == "paper":
    print("Computer win.")
elif user == "paper" and computer == "scissors":
    print("Computer win.")

# invalid case
else:
    print("Invalid input. Try again")