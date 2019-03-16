# A programming doing exercises working with dictionaries
# Carsen Weinzetl 03/06/2019


# Making a dictionary for information about a person
# and then printing all the information from the dictionary
person = {
	'age': '12',
	'sex': 'male',
	'name': 'Timmy',
	'favecolor': 'Red'
	}

# Printing each key and respective value with a for loop
for key, value in person.items():
	print(key + ': ' + value)

print('\n')


# Making a dictionary for peoples favorite numbers and printing them
f_numbers = {
	'John': 2,
	'Dude': 9001,
	'Mr. Game n Watch': 9,
	'Bob': 145
}

# Printing each persons favorite number with a for loop
for key, value in f_numbers.items():
	print(str(key.title()) + "'s favorite number is " + str(value) + "!")

print('\n')


# Making a dictionary as a 'glossary' for new programming terminology
glossary = {
	'For loop': 'A function that will run through any specified container.',
	'Variable': 'A container for information of any kind',
	'Dictionary': 'A container for infinate types of information'
}

# Printing each term and its definition
for key, value in glossary.items():
	print(str(key.title()) + ': ' + str(value))


print('\n')

# Picking out the values with a loop 
print('Some of the phrases I know so far are: ')

for terms in glossary.keys():
	print(str(terms))