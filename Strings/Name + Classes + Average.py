name = str(input("What is your name? "))
numberOfClasses = int(input("How many classes are you taking? "))
average = float(input("What is your average? "))

if average <= 100:
    print("Your name is ", name, ", you are taking ", numberOfClasses, " classes", " and your average is ", average, "%.", sep = "")
else:
    print("YOUR AVERAGE CAN NOT BE GREATER THAN 100%")
