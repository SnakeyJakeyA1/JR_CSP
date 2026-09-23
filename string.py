# JR, String notes

first_name = 'Jake'
last_name = "Rodriguez"

# Concatenation - Add two strings together.
name = first_name + " " + last_name
# Escape char ;ets the progroam ignore the next character in the string
print(f'Ms. LaRose told the class, "You can\'t drive my car. But {name} can."')

user = input("Please tell me your name:\n").strip().title()
print(f"new user recognized\nWelcome {user}")

sentence = "The quick brown fox jumps over the lazy dog."
print(f"The sentence is {len(sentence)} characters long.")
print(sentence)
print(sentence.replace("dog",name))