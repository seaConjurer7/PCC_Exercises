# A small program for practice with numerical lists
# Carsen Weinzetl 02/21/2019

# Counting to twenty with a loop
print("Printing up to 20 in 5 increments:\n")

for twenty in range(0,21,5):
	print(twenty)

print("\n")

# Counting to one million in 100,000 increments to save time
print("Printing up to 1000000 in 100000 increments:\n")

for million in range(100000,1000001,100000):
	print(million)

print("\n")

# Finding the sum, min, & max of a list with one million numbers. 
print("Printing the sum of 1-1000000, the min, and max:\n")


list = [value*1 for value in range(0, 1000001)]
print(sum(list))
print(min(list))
print(max(list))

print("\n")

# Printing the odd numbers of a list from 1 to 20
print("Printing odd numbers from a list 1 to 20:\n")

for odds in range(1,21,2):
	print(odds)

print("\n")

# Making a list with multiples of 3; from 3 to 30 
print("Printing multiples of 3, up to 30:\n")

for multiples in range(3,31,3):
	print(multiples)

print("\n")

# Printing the numbers in a list 1-10 cubed
print("Printing 1-10 cubed:\n")

for cubes in range(1, 11):
	print(cubes**3)

print("\n")

# Printing the numbers in a list 1-10 cubed using a list conprehension
print("Priting 1-10 cubed with a list comprehension:\n")

lccube = [value**3 for value in range(1,11)]
print(lccube)

print("\n")