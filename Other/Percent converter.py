# Percent converter
response = "y"

while response == "y" or response == "Y":
    number = int(input("Please enter a number: "))
    while number < 0:
        number = int(input("Your number must be positive, please enter another number: "))
    percent = str(number * 100) + "%"
    print(percent)
    response = input("Do you want to convert another number? (y/n): ")
