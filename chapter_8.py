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

#

