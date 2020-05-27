num1 = int(input("First number: "))
num3 = int(input("Second number: "))
num2 = num1 // num3
num4 = num1 - num2 * num3

print(num1, num2, num3, num4)

while num4 != 0:
    num1 = num3
    num3 = num4
    num2 = num1 // num3
    num4 = num1 - num2 * num3
    print(num1, num2, num3, num4)

print("\nGCD is:", num3)
