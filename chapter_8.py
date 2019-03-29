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