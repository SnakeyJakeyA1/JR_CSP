# Your budget assignment

while True:
    income = (input("What is your monthly income: $")).strip()
    if income.isalpha():
        print("That isn't a number.")
    elif " " in income:
        print("Just a number!")
    else:
        break

while True:
    rent = input(f"What is your monthly rent: $")
    if rent.isalpha():
        print("That isn't a number.")
    elif " " in rent:
        print("Just a number!")
    else:
        break

while True:
    utilities = input(f"What is your monthly utilities: $")
    if utilities.isalpha():
        print("That isn't a number.")
    elif " " in utilities:
        print("Just a number!")
    else:
        break

groceries = input(f"What is your monthly groceries: $")

transportation = input(f"What is your monthly transportation: $")

input(f"Your rent is ${rent} and that is  of your income")