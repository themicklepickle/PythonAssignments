again = "y"

while again == "y":
    number = int(input("Please enter a number: "))
    print(number * "*")
    again = str(input("Do you want to try again? (y/n) "))

print("Goodbye!")
