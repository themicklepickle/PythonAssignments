# asks user for a grade and repeats it back to them

grade = int(input("Please enter the grade (0 - 100): "))

while grade < 0 or grade > 100:
    grade = int(input("That is not a valid grade, please enter a grade between 0 - 100: "))

print("Your grade is", grade)

"""
#scenarios

x = 9
while x >= 0:
    print(x)
    x -= 10
"""
