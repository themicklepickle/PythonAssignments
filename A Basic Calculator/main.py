# Assignment - A Basic Calculator
# Add, subtract, multiply, divide, modulus, gcd, prime
# Interface module
# Michael Xu
# March 22, 2020

# import other modules
import basic_operations as basic
import bonus_operations as bonus
import sanitization


def operation(sign, function):
    print(f"\n[first number] {sign} [second number] (numbers must be whole numbers)")
    num1 = sanitization.integer("Please enter the [first number]: ", 1, None)
    num2 = sanitization.integer("Please enter the [second number]: ", 1, None)
    result = function(num1, num2)
    print(f"{num1} {sign} {num2} = {result}")
    print(num1 // num2)


def gcd():
    print("\ngcd of [first number] and [second number] (numbers must be whole numbers)")
    num1 = sanitization.integer("Please enter the [first number]: ", 1, None)
    num2 = sanitization.integer("Please enter the [second number]: ", 1, None)
    result = bonus.gcd(num1, num2)
    print(f"gcd of {num1} and {num2} = {result}")


def prime():
    print("\nis [number] prime or composite? (number must be a whole number)")
    num = sanitization.integer("Please enter the [number]: ", 1, None)
    result = bonus.prime(num)
    print(f"{num} is {result}")


# print options for operation
print("1 | add\n2 | subtract\n3 | multiply\n4 | divide\n5 | modulus\n6 | gcd\n7 | prime")

# input operation
option = sanitization.integer("Please enter the operation (1/2/3/4/5/6/7): ", 1, 7)

if option == 1:  # addition
    operation("+", basic.add)
if option == 2:  # subtraction
    operation("-", basic.subtract)
if option == 3:  # multiplication
    operation("*", basic.multiply)
if option == 4:  # division
    operation("/", basic.divide)
if option == 5:  # modulus
    operation("%", basic.modulus)
if option == 6:  # GCD
    gcd()
if option == 7:  # prime
    prime()
