# JR, Password Strength Checker assignment

password = input("What is your password: ")
number = False
upper = False
lower = False
symbol = False

symbols = "!@#$%^&*"

length = len(password) >=8

for letter in password:
    if letter.isnumeric():
        number = True
    if letter.islower():
        lower = True
    if letter.isupper():
        upper = True
    if letter in symbols:
        symbol = True

rules_met = 0

if length:
    rules_met = rules_met + 1

if upper:
    rules_met = rules_met + 1

if lower:
    rules_met = rules_met + 1

if number:
    rules_met = rules_met + 1

if symbol:
    rules_met = rules_met + 1

if rules_met < 3:
    strength = "Weak"
elif rules_met < 5:
    strength = "Medium"
else:
    strength = "Strong"

print(f"At least 8 characters: {length}")
print(f"Has a lowercase letter: {lower}")
print(f"Has an uppercase letter: {upper}")
print(f"Has a number: {number}")
print(f"Has a symbol: {symbol}")
print(f"Your password strength is: {strength}")

if not length:
    print("To make it strong, make it at least 8 charaters.")

if not lower:
    print("To make it strong, add a lowercase letter.")

if not upper:
    print("To make it strong, add an uppercase letter.")

if not number:
    print("To make it strong, add a number.")

if not symbol:
    print("To make it strong, add a symbol.")