#user inputs the first operand
number1 = float(input("Please enter the first operand: "))

#user inputs the second operand
number2 = float(input("Please enter the second operand: "))

#user inputs the operator that they wish to use
operator = input("Please enter an operator (+,-,*,/): ")

#ensures that the operator is either "+", "-", "*" or "/"
while operator != "+" and operator != "-" and operator != "*" and operator != "/":
    operator = input("Invalid operator, please enter another operator (+,-,*,/): ")

#runs if the first number is an integer
if number1 % 1 == 0:
    number1 = int(number1) #converts the float to an integer

#runs if the second number is an integer
if number2 % 1 == 0:
    number2 = int(number2) #converts the float to an integer

#runs if the operator is an addition sign ("+")
if operator == "+":
    addition = number1 + number2 #the sum of the two numbers is calculated
    print(number1, "+", number2, "=", addition) #the sum is printed

#runs if the operator is a subtraction sign ("-")
elif operator == "-":
    subtraction = number1 - number2 #the difference of the two numbers is calculated
    print(number1, "-", number2, "=", subtraction) #the difference is printed

#runs if the operator is a multiplication sign ("*")
elif operator == "*":
    multiplication = number1 * number2 #the product of the two numbers is calculated
    print(number1, "*", number2, "=", multiplication) #the product is printed

#runs if the operator is a division sign ("/")
else:
    division = number1 / number2 #the quotient of the two numbers is calculated
    print(number1, "/", number2, "=", division) #the quotient is printed
