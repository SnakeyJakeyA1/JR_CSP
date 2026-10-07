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
            number = ord(letter)+shift
            result += chr(number)
            if number > ord("Z") and letter.isupper():
                number -= 26
            elif number > ord("z") and letter.islower():
                number -= 26
        else:
            result += letter
    return result



if e_d == "E":
    print(cipher(message, shift))
