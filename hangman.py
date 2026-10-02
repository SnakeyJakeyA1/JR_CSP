# JR, Hangman assignment

import random

with open('hangman.txt' "r") as file:
    content = file.read()
    words = content.split(",")
    word = random.choice()
    print(content)
