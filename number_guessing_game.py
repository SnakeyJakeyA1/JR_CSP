# JR, Number Guessing game assignment

import random
count = 0
number = random.randint(1,100)

print("I'm thinking of a number between 1 and 100. You have six tries to guess it!")

while count <= 6:
    guess = int(input("What is your guess?: "))
    print(guess)
    count += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    elif guess == number:
        print(f"You guessed right! You guessed it in {count - 1} tries.")
        break
    if count == 6:
        print(f"You ran out of guesses! The number was {number}.")
        break
