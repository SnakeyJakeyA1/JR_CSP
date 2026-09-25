# JR, Number Guessing game assignment

import random
guess = 1

while guess <= 6:
    print(guess)
    guess += 1

number = random.randint(1,100)


while True:
    print(number)
    if 