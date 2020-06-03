number = int(input("Please enter a number: "))

number1 = 0
number2 = 1

for x in range(1, number):
    oldNumber2 = number2
    number2 += number1
    number1 = oldNumber2

print("The ", number, "th Fibonacci number is ", number2, sep="")
