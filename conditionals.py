# JR, Conditionals Notes

military_time = 900

if military_time > 600:
    print("It's still early")
elif military_time < 900:
    print("And you're still FAT")
elif military_time < 1200:
    print("Breakfast formation")
elif military_time < 1700:
    print("I WANNA SEE SOME REAL CAVEMAN OUT THERE. We do this fast, we do this loud, we do this as a family")
else:
    print("And never, not, be afraid!")

# nesting conditionals
day = "Saturday"
time = 1300

if time > 900 and time < 1600:
    if day != "Saturday" or day != "Sunday":
        print("You should be at school!")
    else:
        if time > 1200:
            print("Good afternoon!")
        else:
            print("Good morning!")
else:
    print("You aren't required to be at school.")