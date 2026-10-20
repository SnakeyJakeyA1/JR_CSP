import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("🎲 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Type 'roll' to reveal the number.")
print("Type 'quit' to exit the game.")

while True:
    guess = input("\nEnter your guess: ").strip().lower()

    # Reveal the random number
    if guess == "roll":
        print(f"🎲 The random number is {secret_number}!")
        break

    # Exit the game
    if guess == "quit":
        print("Thanks for playing!")
        break

    # Check whether the input is a valid number
    if not guess.isdigit():
        print("Please enter a number, 'roll', or 'quit'.")
        continue

    guess = int(guess)

    if guess < 1 or guess > 100:
        print("Your guess must be between 1 and 100.")
        continue

    attempts += 1

    if guess < secret_number:
        print("📈 Too low! Try a higher number.")
    elif guess > secret_number:
        print("📉 Too high! Try a lower number.")
    else:
        print(f"🎉 Correct! The number was {secret_number}.")
        print(f"You guessed it in {attempts} attempt(s)!")
        break