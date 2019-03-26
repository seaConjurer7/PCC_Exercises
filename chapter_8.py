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




