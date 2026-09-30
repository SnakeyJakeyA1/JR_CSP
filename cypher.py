# JR, cipher assignment

# Define Variables
e_d = input("Would you like to (E)ncrypt or (D)ecrypt a message?: ")
message = input("What is your message?: ")
shift = int(input("Enter shift amount: "))

# Write the function
for letter in message:
    if letter.isalpha():
        letter = ord(letter)

