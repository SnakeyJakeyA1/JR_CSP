# JR, cipher assignment

# Define Variables
e_d = input("Would you like to (E)ncrypt or (D)ecrypt a message?: ")
message = input("What is your message?: ")
shift = int(input("Enter shift amount: "))

# Write the function
def cipher(message, shift):
    result = ""

    for letter in message:
        if letter.isalpha():
            number = ord(letter)

            if letter.isupper():
                start = ord("A")
            else:
                start = ord("a")

            position = (number - start)
            position_2 = (position + shift) %26

