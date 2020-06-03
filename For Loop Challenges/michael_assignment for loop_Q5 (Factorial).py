number = int(input("Please enter a number: "))

print(number, "! = ", sep="", end="")

factorial = 1

for x in range(1, number + 1):
    factorial *= x
    if x == number:
        print(number - x + 1, " ", sep="", end="")
    else:
        print(number - x + 1, " x ", sep="", end="")

print("= ", factorial, ".", sep="")
