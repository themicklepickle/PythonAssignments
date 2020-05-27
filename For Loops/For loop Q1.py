#With append
list1 = []
for x in range(6):
    list1.append(x)
print(list1)

list1 = []
for x in range(1, 6):
    list1.append(x)
print(list1)

list1 = []
for x in range(-4, 5, 2):
    list1.append(x)
print(list1)

list1 = []
for x in range(4, -1, -2):
    list1.append(x)
for x in range(-2, 5, 6):
    list1.append(x)
print(list1)


print("\n\n")

#With list[x] = x
list1 = [0,0,0,0,0,0]
for x in range(6):
    list1[x] = x
print(list1)

list1 = [0,0,0,0,0]
for x in range(1, 6):
    list1[x-1] = x
print(list1)

list1 = [0,0,0,0,0]
for x in range(-4, 5, 2):
    list1[x] = x
print(list1)

list1 = [0,0,0,0,0]
for x in range(4, -5, -2):
    list1[x] = x
print(list1)
