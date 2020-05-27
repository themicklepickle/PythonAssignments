name = str(input("Enter a name: "))
name = list(name)
length = len(name)

program = input("Choose a program (1/2): ")

letter = name[0].upper()
print(letter, end = "")

count = 1

if program == "1":
    while count < length:
        letter = name[count].lower()
        print(letter, end = "")
        count += 1
if program == "2":
    while count < length:
        if count % 2 > 0:
            letter = name[count].lower()
            print(letter, end = "")
            count += 1
        else:
            letter = name[count].upper()
            print(letter, end = "")
            count += 1
