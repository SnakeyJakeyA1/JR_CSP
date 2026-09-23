# JR, Password Strength Checker assignment

password = input("What is your password: ")
length = "False"
number = "False"
characters = "False"
upper = "False"
lower = "False"
symbol = "False"


if len(password) >=8:
    print(password)
else:
    print(length)

if password.isnumeric():
    print("You're missing an upercase and lowercase letter")

if " " in password:
    print("Your password can't have spaces")

if password.islower():
    print("You are missing an uppercase letter")

if password.isupper():
    print("You are missing a lowercase letter")

if password.isalpha():
    print("You are missing a number")
