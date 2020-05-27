hourlyWage = float(input("What is your hourly wage? "))
hoursWorked = float(input("How many hours did you work? "))

if hoursWorked <= 40:
    pay = hourlyWage * hoursWorked
    pay = str("%0.2f" % pay)
    print("Your pay is $" + pay)
else:
    pay = hourlyWage * 40 + hourlyWage * 1.5 * (hoursWorked - 40)
    pay = str("%0.2f" % pay)
    print("Your pay is $" + pay)
