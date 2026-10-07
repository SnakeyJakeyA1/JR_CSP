# JR, Reading and Writing to Files Notes

with open('practice.txt', "r") as file:
    # "r" = read
    content = file.read()
    print(content)
    word = content.find("Rodriguez")
        # Finds the word "Rodriguez" in the document
    length = len("Rodriguez")
    content += " Treyson!"
    file.write(content)
        # The .upper() only makes the changes in the code. Not the document.
    
with open("practice.txt", "w") as file:
    # "w" = write
    file.write("Hello")
        # .write lets you replace everything in the document.

