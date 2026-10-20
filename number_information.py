# JR, Number information assignment

for number in range(1,21):
    if number%5 == 0:
        devide5 = "is divisible by 5"
    else:
        devide5 = "is not divisible by 5"
    if number%2 == 0:
        evodnum = "even"
    else:
        evodnum = "odd"

    print(f"{number} is {evodnum} and {devide5}")