def f(x):
    x += 1
    print("In function: {0}".format(x))


x = 5
print("Before function: {0}".format(x))
f(x)
print("After function: {0}".format(x))
