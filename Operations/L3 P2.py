#initial amount
numberOfBacteria = 100

#growth rate per hour
growthRate = 2 / 1.25

#hour 0
print("The initial amount of bacteria is", int(numberOfBacteria))

#hour 1
numberOfBacteria *= growthRate
print("After 1 hour, there are now", int(numberOfBacteria), "bacteria cells")

#hour 2
numberOfBacteria *= growthRate
print("After 2 hours, there are now", int(numberOfBacteria), "bacteria cells")

#hour 4
numberOfBacteria *= growthRate
print("After 3 hours, there are now", int(numberOfBacteria), "bacteria cells")

#hour 5
numberOfBacteria *= growthRate
print("After 4 hours, there are now", int(numberOfBacteria), "bacteria cells")


#using a loop

print()
print("Now Using a Loop!")

#initial amount
numberOfBacteria = 100

#growth rate per hour
growthRate = 2 / 1.25

print("The initial amount of bacteria is", int(numberOfBacteria))

hours = 1

i = 1
while i < 5:
    if hours == 1:
        numberOfBacteria *= growthRate
        print("After", hours, "hour, there are now", int(numberOfBacteria), "bacteria cells")
    else:
        numberOfBacteria *= growthRate
        print("After", hours, "hours, there are now", int(numberOfBacteria), "bacteria cells")
    hours +=1
    i += 1
