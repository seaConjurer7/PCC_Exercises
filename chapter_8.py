# A small program for practicing concepts learned in chapter 8 
# Carsen Weinzetl 03.19.2019

# ------------------------------------------- #

# Making a function that greets people
def greet_user():
	'''Display a simple greeting'''
	print('Hello!')

# Calling the function
greet_user()

# ------------------------------------------- #

# Making a function that calls someone with a parameter
def greet_user(username):
	'''Display a custom greeting'''
	print('\nHello, ' + username.title() + '!')

# Calling the function with a parameter
greet_user('Jesse')

# ------------------------------------------- #

# Making a function that prints a message taking two parameters
def pets(animal_type, pet_name):
	print('\nI have a ' + animal_type + '.')
	print('My ' + animal_type + "'s name is, " + pet_name.title() + '!')

# Calling the function twice, with different parameters
pets('Dog', 'Spaghetti')
pets('Cat', 'Pumpernickel')

# ------------------------------------------- #

# Remaking the function above with keyword arguments 
# to ensure no mixup in the order of inputs
def describe_pet(animal_type, pet_name):
	'''Display info about pet'''
	print('\nI have a ' + animal_type + '.')
	print('My ' + animal_type + "'s name is " + pet_name.title() + '.')

# Calling the function ensuring that the order no longer matters
describe_pet(animal_type='Hamster', pet_name='Bob')
describe_pet(pet_name='Bob',animal_type='Hamster')

# ------------------------------------------- #

# Making a function that takes a first and last name,
# and returns a neatly formatted name
def formatted_name(first_name, last_name):
	'''Return full name neatly formatted'''
	full_name = first_name + ' ' + last_name
	return full_name.title()

# Calling the function with multiple values 
canidate = formatted_name('\nBernie', 'Sanders')
print(canidate)

president = formatted_name('Donald', 'Trump')
print(president)

# ------------------------------------------- #

# Making a function that makes makes an argument optional
# using the same name formatting theme above, with an optional
# argument for the middle name
def optional_format(first_name, last_name, middle_name=''):
	'''Checking for input'''
	if middle_name: 
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name

	return full_name.title()

# Calling the function with an optional middle name
middleName = optional_format('Billy', 'Joe', 'Bob')
noMiddleName = optional_format('Billy', 'Joe')

print(middleName)
print(noMiddleName)

# ------------------------------------------- #

# Making a function that uses a dictionary, to build a
# portfolio of information for a person
print('\n')

def buildPerson(first_name, last_name, age=''):
	'''Return a dictionary of information about a person'''
	person = {
		'first': first_name, 
		'last': last_name
	}

	if age:
		person['age'] = age
	return person

# Calling the function & adding an age to the dictionary
myself = buildPerson('Carsen', 'Weinzetl', age=19)
print(myself)

# ------------------------------------------- #

# Making a function that uses a while loop to take down peoples names
# and then formats them neatly
def name_formatter(first_name,last_name):
	'''Return full name, neatly formatted'''
	full_name = first_name + ' ' + last_name
	return full_name.title()

while True:
	print('\nPlease tell me your name:')
	print('(enter q at any time to quit)')

	first_name = input('First name: ')
	if first_name == 'q': 
		break
	last_name = input('Last name: ')
	if last_name == 'q': 
		break

# ------------------------------------------- #

# Passing lists to a function, making a program that creates custom messages
# with peoples names that are stored in a list. 
print('\n')

def greet_users(names):
	'''Print a simple greeting to each user in the list'''
	for name in names:
		msg = 'Hello, ' + name.title() + '!'
		print(msg)

# Defining two lists to pull from
usernames = ['Carsen', 'Jeremy', 'Spaghetti']
other_usernames = ['Eragon', 'Smaug', 'Elvarg']

# Calling the function using two different lists
greet_users(usernames)
print('\n')
greet_users(other_usernames)

# ------------------------------------------- #

# A program that tracks people orders being made using lists, and no functions
print('\n')

# Orders that are not completed, and a list for orders that are done
uncompleted_orders = ['5 Donuts', 'Lrg Machiato and 1 Bagel', 'Lrg Spaghetti']
completed_orders = []

# Simulating every order being completed until none or left
while uncompleted_orders:
	current_order = uncompleted_orders.pop()

	# Simulating creating an order
	print('Completing order for: ' + current_order)
	completed_orders.append(current_order)

# Show all completed orders
print('\nThe following orders have been completed: ')
for completed_order in completed_orders: 
	print(completed_order)

# ------------------------------------------- #

# Re-writting the previous program using functions 
print('\n')

def print_orders(uncompleted_orders, completed_orders):
	'''
	Simulating completing each order, until none are left.
	Move each order to the completed_orders after completing.
	'''
	while uncompleted_orders: 
		current_order = uncompleted_orders.pop()

		# Simulating completing an order
		print('Completing order: ' + current_order)
		completed_orders.append(current_order)

def show_completed_orders(completed_orders): 
	'''Show all the orders that have been finished'''
	print('\nThe following orders have been completed: ')
	for completed_order in completed_orders: 
		print(completed_order)

# Defining uncompleted and completed orders
uncompleted_orders = ['5 Donuts', 'Lrg Machiato and 1 Bagel', 'Lrg Spaghetti']
completed_orders = []

# Calling the functions 
print_orders(uncompleted_orders, completed_orders)
show_completed_orders(completed_orders)

# ------------------------------------------- #

# Making a function that can accept multiple arguments 

print('\n')

def make_pizza(*toppings): 
	'''Sumarising the pizza and its toppings'''
	print('\nMaking a pizza with the following toppings: ')
	for topping in toppings: 
		print('- ' + topping)

make_pizza('Spaghetti')
make_pizza('Mushroom', 'Steak', 'Garlic Bread', 'Lilac')

# ------------------------------------------- #

# Making a function that can accept both a
# positional argument, and an arbitrary argument

print('\n')

def make_pizzaa(size, *toppings):
	'''Sumarizing the pizzas size and its toppings'''
	print('Making a ' + str(size) + 
		'-inch pizza with the following toppings: ')
	for topping in toppings: 
		print('- ' + topping)

make_pizzaa(420, 'Weed')
make_pizzaa(12, 'Pickles', 'Peanut Butter')

# ------------------------------------------- #

# Using arbitrary keyword arguments

print('\n')

def build_profile(first, last, **user_info): 
	'''Building a dictionary containing everything we know about a user'''
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value 
	return profile

# Creating a variable that calls the function
user_profile = build_profile('Carsen', 'Weinzetl', 
	location = 'Barksdale AFB', AFSC = '1W0X1')

# Printing the variable to the console
print(user_profile)

# ------------------------------------------- #

# Importing a module, and using functions from the module

import pizzamodule

pizzamodule.make_pizza(12, 'Cheese')

# ------------------------------------------- #

# Importing a specific function, from a module

'''

from pizzamodule import make_pizza

make_pizza(12, 'Cheese')

'''

# ------------------------------------------- #

# Importing a module using 'as' to give the module an alias

'''

from pizzamodule import make_pizza as mp

mp(12, 'Cheese')

'''

# ------------------------------------------- #

# Using 'as' to give a module an alias

'''

import pizzamodule as p

p.make_pizza(12, 'Cheese')

'''

# ------------------------------------------- #

# Importing all functions from a module 

'''

from pizzamodule import *

make_pizza(12, 'Cheese')

'''

# ------------------------------------------- #


