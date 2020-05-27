# create a string - composite = space, prime = *
x = int(input("Please enter a number: "))

prime_string = "|"

for i in range(2, x + 1):
    is_prime = True
    for div in range(2, i):
        if i % div == 0:
            is_prime = False
    if is_prime == True:
        prime_string += "*"
    else:
        prime_string += " "

prime_string = prime_string + "|"

print(prime_string)
