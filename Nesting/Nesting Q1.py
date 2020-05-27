maximum = int(input("Please enter a maaximum number: "))
divisibility = int(input("Please enter a divisibility number: "))

for i in range(1, maximum + 1):
    if i % divisibility == 0:
        print(i)
