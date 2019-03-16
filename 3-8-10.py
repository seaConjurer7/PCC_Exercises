# A small program messing with lists about place all around the world
# Carsen Weinzetl 02/20/2019

# Making the list and printing it to the console
places = ["FL", "AK", "AR", "GA", "WI"]

print("Printing the original list:")

print(places)
print("\n")

# Printing the list in alphabetical order & showing that it is still unchanged
print("Printing the places in alphabetical order, and then the original order:")

print(sorted(places))
print(str(places))
print("\n")

# Printing the list in reverse non permently & showing that it is still unchanged
print("Printing the places in reverse alphabetical order, and then the original order:")

print(sorted(places, reverse = True))
print(str(places))
print("\n")

# Printing a reversed list, and then reversing it back to normal
print("Printing the reversed order, and then reversing again to original order:")

places.reverse()
print(places)

places.reverse()
print(places)

print("\n")

# Printing a permanent alphabetical sort, and then a permanent reverse alphabetical sort
print("Printing a permently alphabetical sort, and then a permently reverse alphabetical sort:")

places.sort()
print(places)

places.sort(reverse=True)
print(places)
