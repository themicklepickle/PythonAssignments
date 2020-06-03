number = int(input("Please enter a number: "))
count = 1

print("Factors are ", end="")

while count <= number:
    if number % count == 0:
        print(count, end=" ")
    count += 1
