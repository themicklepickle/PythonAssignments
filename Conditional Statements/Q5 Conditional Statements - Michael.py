# user enters hourly wage
hourlyWage = float(input("Please enter your hourly wage: "))

# ensures that the hourly wage is greater than zero
while hourlyWage <= 0:
    hourlyWage = float(input("Sorry, your hourly wage must be greater than zero, please enter another number: "))

# user enters number of hours worked
hoursWorked = float(input("Please enter the number of hours you worked: "))

# ensures that the number of hours worked is greater than zero
while hoursWorked <= 0:
    hoursWorked = float(input("Sorry, your hours worked must be greater than zero, please enter another number: "))

# runs if the number of hours worked is less than or equal to 40
if hoursWorked <= 40:
    pay = hourlyWage * hoursWorked  # calculates pay
    pay = str("%0.2f" % pay)  # converts the float to a 2 decimal place number because that is how currency is represented
    print("Your pay is $" + pay + ".")  # prints the pay
elif hoursWorked <= 60:
    pay = hourlyWage * 40 + hourlyWage * 1.5 * (hoursWorked - 40)  # calculates pay
    pay = str("%0.2f" % pay)  # converts the float to a 2 decimal place number because that is how currency is represented
    print("Your pay is $" + pay + ".")  # prints the pay
else:
    pay = hourlyWage * 40 + hourlyWage * 1.5 * 20  # calculates pay
    pay = str("%0.2f" % pay)  # converts the float to a 2 decimal place number because that is how currency is represented
    print("Your pay is $" + pay + ".")  # prints the pay
    if hoursWorked > 60:
        unpaidHours = hoursWorked - 60  # calculates the number of unpaid hours
        print("Your last", unpaidHours, "hours are unpaid.")  # prints the number of unpaid hours
