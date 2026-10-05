# JR, Hangman assignment

import random

words = []

with open('hangman.txt', "r") as file:
    content = file.read()
    print(content)

print(words)

with open('hangman.txt', "r") as file:
    words.append('lapy')