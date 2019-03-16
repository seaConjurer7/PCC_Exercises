# A small program practicing using conditional tests
# Carsen Weinzetl 02/04/2019

# Making 10 conditional tests with half n' half being true n' false


# -1-
lifeAwnser = 42
print('Is the awnser to life 42? I predict true.')
print(lifeAwnser == 42)

print('Is the awnser to life 9999? I predict true.')
print(lifeAwnser == 9999)

print('\n')


# -2-
lifeAwnser1 = 246
print('Is the awnser to life 246? I predict true.')
print(lifeAwnser1 == 246)

print('Is the awnser to life 9999? I predict true.')
print(lifeAwnser1 == 9999)

print('\n')


# -3-
lifeAwnser2 = 25
print('Is the awnser to life 25? I predict true.')
print(lifeAwnser2 == 25)

print('Is the awnser to life 9999? I predict true.')
print(lifeAwnser2 == 9999)

print('\n')


# -4-
lifeAwnser3 = 34
print('Is the awnser to life 34? I predict true.')
print(lifeAwnser3 == 34)

print('Is the awnser to life 9999? I predict true.')
print(lifeAwnser3 == 9999)

print('\n')


# -5-
lifeAwnser4 = 12
print('Is the awnser to life 12? I predict true.')
print(lifeAwnser4 == 12)

print('Is the awnser to life 9999? I predict true.')
print(lifeAwnser4 == 9999)

print('\n')


# More conditionals tests using slightly different approaches


# Testing inequality with strings
string = 'Spaghetti'
print('Is string == "Spaghetti"? I predict true.')
print(string == 'Spaghetti')

print('Is string == "Canoli"? I predict false.')
print(string == 'Canoli')

print('\n')


# Testing inequality with lower()
lower = 'AAAA'
print('Is lower.lower() == aaaa, I predict true.')
print(lower.lower() == 'aaaa')

print('Is lower.lower() == AAAA, I predict false.')
print(lower.lower() == 'AAAA')

print('\n')


# Testing inequality with operators 
number = 9
print('Is number > 1, I predict true.')
print(number > 1)

print('Is number == 1, I predict false.')
print(number == 1)

print('\n')


# Testing inequality with 'and' & 'or' keywords
var = 12
print('Is var == 12 and var < 20? I predict true.')
print(var == 12 and var < 20)

print('Is var == 13 or var < 20? I predict true.')
print(var == 13 or var < 20)

print('\n')

# Testing inequality for wether or not something is in a list
things = (35, 25, 45, 55)

print('Is the number 25 2nd in the list? I predict true.')
for number in things:
	print(number == 25)

print('\n')

print('Is the number 345251 4th in the list? I predict false.')
for number in things:
	print(number == 345251)

