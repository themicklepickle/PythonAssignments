import student_module as sm

user_num = int(input("Please enter a number: "))

prime  = 1
decomp_string = ""

while prime < user_num:
    prime = sm.next_prime(prime)
    if user_num % prime == 0:
        num_divs = sm.num_times_divisible(user_num, prime)
        decomp_string = decomp_string + ("" if len(decomp_string) == 0  else " ") + str(prime) + "^" + str(num_divs)

print(decomp_string)