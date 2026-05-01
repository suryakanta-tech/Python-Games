# number guessing game

import random

number = random.randint(1,100)

print("Guess the number between 1 to 100....")
print("You have only 5 chancess to guess the number.")

for i in range(5):
    guess = int(input("Enter your guess number: "))
    
    if guess == number:
        print("You Win!")
        break
    elif guess > number:
        print("Too high!")
    else:
        print("Too low!")
else:
    print("You lose the game....")
    print("The number is:",number)