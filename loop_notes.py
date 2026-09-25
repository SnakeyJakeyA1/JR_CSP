# JR, Loops Notes
import random
# Code that will repeat over and over again.
count = 1

while count <= 10:
    print(count)
    count += 1


goose = random.randint(1,17)
ducks = 1

while True:
    print("duck")
    if ducks == goose:
        break
    ducks += 1
print("GOOSE!!!")

siblings = ["Joshua", "Emma", "Jonah", "Isa"]

print(siblings[2])
print(siblings)
# add to the list
item = input("What needs to be added to the list: ")
siblings.append("Spencer")
siblings.insert(4, item)

# remove from list
print(siblings)
print(siblings.pop(5))
print(siblings)

# For Loops
for number in range(1,11,2):
    print(number)

for sibling in siblings:
    print(sibling + " Rodriguez")