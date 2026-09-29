# JR, Funcitons notes

# Examples of functions
# - round()
# - len()
# - print()

def stupid_proof(money):
    while True:
        try:
            temp = float(input(f"What is your monthly {money}?: "))
            return
        except:
            print("That is not a number :(")

# Variables first
income = stupid_proof("income")
rent = stupid_proof("rent")
utilites = stupid_proof("utilites")
transportation = stupid_proof("transportation")
groceries = stupid_proof("groceries")
save = stupid_proof("save")

# Functions second
def calc_percent(bill, income):
    return round(bill/income * 100)
    # "bill/income * 100" are parts of the equaiton that are the parameters.
    # return puts the information at the function call.


print(f"Your rent is ${rent} which is {calc_percent(rent, income)}% of your income")
    # "{calc_percent(rent, income)}" is the function call.
    # "(rent, income)" = "(bill, income)"
print(f"Your utilites is ${utilities} which is {calc_percent(utilities, income)}% of your income")
print(f"Your transportation is ${transportation} which is {calc_percent(transportation, income)}% of your income")
print(f"Your groceries is ${groceries} which is {calc_percent(groceries, income)}% of your income")
print(f"You should save is ${save} which is 10% of your income.")
print(f"That means you have {income-rent-utilities-transportation-groceries-save} left to spend.")
