# A small program for doing the exercises using dictionaries and lists
# Carsen Weinzetl 03/06/2019

# Making a list with multiple dictionaries for multiple people
Bob = {
	'Age': 31,
	'Sex': 'male',
	'Country': 'Canada',
}
Tim = {
	'Age': 24,
	'Sex': 'male',
	'Country': 'Turkey',
}
Jenny = {
	'Age': 21,
	'Sex': 'female',
	'Country': 'UK',
}

people = [Bob, Tim, Jenny]

# Looping through the list and printing everything known about them
for person in people:
	print(str(person))

print('\n')

# Making a list of dictionaries, for people and their favorite places
favorite_places = {
	'Bob': ['China', 'Florida', 'Wisconsin'],
	'Tim': ['Moon', 'Jupiter', 'Mars'],
	'Alfred': ['New York', 'Canada', 'Earth']
}

# Looping through the dictionary listing each person and their fav places
for person, place in favorite_places.items():
	print(str(person) + "'s favorite places are: \n \t" + str(place))

print('\n')

# Making a dictionary with peoples favorite numbers
favorite_numbers = {
	'Bob': ['12', '234'],
	'Tim': ['1345145'],
	'Alfred': ['16661']
}

# Printing each persons name and favorite numbers
for person, number in favorite_numbers.items():
	print(str(person) + "'s favorite numbers are: \n \t" + str(number))

