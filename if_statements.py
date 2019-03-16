# A small program going through the exercises in the 'if statements' chapter
# Carsen Weinzetl 03/05/2019

# If statements about voting 
age = 19

if age >= 18:
	print('You are old enough to vote.')
	print('Have you registered to vote?')
else:
	print('You are too young to vote.')
	print('You can registar to vote once you turn 18.')

print('\n')

# If statements for prices at an amuesment park
age = 12

if age < 4:
	print('Your ticket will cost 0$')
elif age < 18:
	print('Your ticket will cost 5$')
else: 
	print('Your ticket will cost 10$')

print('\n')

# Making the same program but with multiple 'elif' statements, and-
# omitting the 'else' statement
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
elif age > 65:
	price = 5

print('Your ticket will cost ' + str(price) + '$')

print('\n')

# Testing multiple conditions 
print('Alright, what toppings were requested on this pizza?')

requested_toppings = ['mushrooms', 'pineapple']

if 'mushrooms' in requested_toppings:
	print('Adding mushrooms to your pizza...')
if 'pineapple' in requested_toppings: 
	print('Adding pineapple to your pizza...')

print('Your pizza is ready!')

