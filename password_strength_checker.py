# JR, Password Strength Checker assignment

password = input("What is your password: ")
number = "False"
characters = "False"
upper = "False"
lower = "False"
space = "False"
symbol = "False"

symbols = "!@#$%^&*"

length = len(password) >=8

for letter in password:
    if password.isnumeric():
        print(number)
    if " " in password:
        print(space)
    if password.islower():
        print(upper)
    if password.isupper():
        print(lower)
    if password.isalpha():
        print(characters)

rules_met = 0

if length:
    rules_met = rules_met + 1

if upper:
    rules_met = rules_met + 1

if lower:
    rules_met = rules_met + 1

if space:
    rules_met = rules_met + 1

if characters:
    rules_met = rules_met + 1

if number:
    rules_met = rules_met + 1

if symbol:
    rules_met = rules_met + 1