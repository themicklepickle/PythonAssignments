number = int(input("Enter a number: "))

remainder2 = number % 2
remainder3 = number % 3

if remainder2 < 1 and remainder3 < 1:
    print("bloop")
elif remainder3 < 1:
    print("bleep")
elif remainder2 < 1:
    print("blip")
