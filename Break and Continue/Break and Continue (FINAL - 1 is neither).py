# Q1 Assignment - break and continue
# Program that determines whether or not a number is prime using break or continue
# Michael Xu

# input user number
num = int(input("Please enter a whole number: "))

# accounts for edge cases of num = 1 and num = 2 where the for loop doesn't work
if num == 1:
    print(num, "is neither a prime nor composite number")
elif num == 2:
    print(num, "is a prime number")

# checks every number in the range from 2 to the number - 1
for i in range(2, num):

    # if i divides evenly into num
    if num % i == 0:
        # outputs that it is a composite number
        print(num, "is a composite number")
        # breaks the loop and the program ends
        break

    # if i is the last number in the range
    if i == num - 1:
        # outputs that it is a prime number
        print(num, "is a prime number")
