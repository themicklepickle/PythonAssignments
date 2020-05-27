# Assignment - lists and tuples
# Q4 - Given an array of ints named num_list, write a code snippet to calculate the mean of the values.
# Michael Xu
# 21 April 2020

# initiate list of ints: num_list
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# get the sum of all ints within num_list
total = 0
for num in num_list:
    total += num

# calculate mean by dividing total by the length of num_list
mean = total / len(num_list)

# print result
print("num_list:", num_list)
print("mean:", mean)
