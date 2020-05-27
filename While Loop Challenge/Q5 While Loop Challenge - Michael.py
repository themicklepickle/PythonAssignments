number = int(input("Please enter a number: "))
number += 1
count = 1

while count < number:
    print((number - count) * " " + (count * 2 - 1) * "*")
    count += 1
