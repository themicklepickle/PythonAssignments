while True:
    number = int(input("Please enter a number: "))
    factors = []

    print("\nFactors are", end=" ")

    for x in range(1, number + 1):
        if number % x == 0 and not x in factors:
            factors.append(x)
            print(x, end=" ")
            otherFactor = number // x
            factors.append(otherFactor)
            print(otherFactor, end="\n            ")

    print("\n")

    print("Factors are", end=" ")

    for x in range(1, number + 1):
        if number % x == 0:
            print(x, end=" ")

    print("\n")
