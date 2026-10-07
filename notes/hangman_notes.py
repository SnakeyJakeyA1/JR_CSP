# JR, Hangman notes

import random

# Create a list of 10 words on a seperate txt file  Y

# Create another txt file that only holds the win/loss count    Y

# Use split(",") on the content of the words in the txt documment to create your list of words  

# Pull win and lose totals from the other txt file and save them as 2 seperate variables

# Building the hangman game:

# Save the correct word as a variable random.choice("name_of_list") <----

# Keep trach of:
# The number of wrong guesses
# What letters have been guessed


# Function to display the hangman (Needs number of wrong guesses)
"""______
   |    |
   |    O
   |   /|\\
   |   / \\
   |
   |_________
"""

# Function to show the letters and spaces (The correct word, letters that have been guessed):

# Loop over the correct word
    # Variable for word display (starts as an empty string)
    # Check if letter has been guessed
        # Then add the letter to the word display
    # If they haven't guessed the letter
        # Add an underscore to the word display
# Return the finished word display (outside of the loop)


# Main game loop (while True)
    # Call the function to show the hangman
    # Print function call to show the word display
    # Create variable and ask user to guess a letter
    # Add the letter to our list of guessed letters
    # Check if the letter is not in the word:
        # Increase incorrect guesses
    # Check if word display is the same as the word
        # Tell user they won!
        # Ask if they want to play again
            # Reset the random word, wrong guess count, and increase the win total
    # Check if they lost. Ff they have 6 wrong guesses:
        # Tell them they lost
        # Tell them what the word was
        # Increase the lost count
        # Ask if they want to play again
            # Reset the random word, wrong guess count, and increase the win total

