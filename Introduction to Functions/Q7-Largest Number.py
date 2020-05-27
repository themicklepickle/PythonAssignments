#Assignment - Introduction to Functions
#Q7-Program that asks the user for three numbers and returns the largest one.
#Michael Xu

######### FUNCTIONS #########
def largest_number(num1, num2, num3):
    if num1 - num2 > 0 and num1 - num3 > 0:
        return num1
    
    if num2 - num1 > 0 and num2 - num3 > 0:
        return num2
    
    if num3 - num1 > 0 and num3 - num2 > 0:
        return num3

    if num1 == num2 or num2 == num3 or num1 == num3:
        return "ERROR: ONLY ONE VALUE CAN BE RETURNED. NUMBERS MUST BE DISTINCT."

######## MAIN PROGRAM ########
first_num = int(input("Please enter the first integer: "))
second_num = int(input("Please enter the second integer: "))
third_num = int(input("Please enter the third integer: "))

print("The largest number is", str(largest_number(first_num, second_num, third_num)) + ".")
