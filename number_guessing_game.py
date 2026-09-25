# JR, Number Guessing game assignment

import random
count = 1
number = random.randint(1,100)

while count <= 6:
    guess = input("What is your guess?: ")
    print(guess)
    count += 1
