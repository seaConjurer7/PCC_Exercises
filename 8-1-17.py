# A program for exercises in chapter 8
# Carsen Weinzetl 03.19.2019

# ------------------------------------------- #

# Writing a function called display_message() that prints one sentence
# telling everyone what you are learning about in this chapter. Call the function
# to make sure it works properly 
def display_message():
	print('Hello World!')

# Calling the function
display_message()

# ------------------------------------------- #

# Writting a function that prints a personalized message about someones favorite
# book, then call the function to make sure it works. 
def fav_book(book):
	print('\nMy favorite book is, ' + book + '!')

# Calling the function 
fav_book('"A Time to Kill"')

# ------------------------------------------- #

# Writing a function that accepts a t-shirt size, and the text of a message
# that should be printed on the t-shirt. The function should then print a summary
# of the tshirt itself
print('\n')

def tshirt(size, message):
	print('The shirt is a size, ' + size.lower() + 
	'. That says: ' + message.title())

# Calling the function with positional & keyword arguments
tshirt('Large', 'There is no speed limit in heaven.')

tshirt(
	size = 'Large',
	message = 'There is no speed limit in heaven.'
)

# ------------------------------------------- #

# Rewritting the function above with default messages
def tshirt2():
	print('\nThe shirt is a size, Large. With a message that says: "I love Python!".')

# Calling the function 
tshirt2()

# ------------------------------------------- #

# Writting a function that accepts the name of a city and its country. 
# It should print a simple sentence using the two arguments given. 
print('\n')

def places(city): 
	print(city.title() + ' is in the USA.')

# Calling the function three times, with one of cities not matching the statement
places('Tampa')
places('Boston')
places('Ontario')

# ------------------------------------------- #

# Writting a function that takes a city and a country as an argument, 
# and returns it in order
print('\n')

def city_country(city, country):
	final = city + ', ' + country
	print(final.title())

# Calling the function 
city_country('Clearwater', 'USA')
city_country('Jacksonville', 'USA')
city_country('Miami', 'USA')

# ------------------------------------------- #

# Writting a function that builds a dictionary to describe an album
# then using the function to make three different dictionaries to describe 
# three different albums
print('\n')

def make_album(name, title, numtracks = ''):
	album = {'Artist Name': name, 'Album Title': title }

	if numtracks:
		album['numtracks'] = numtracks

	return album

# Calling the function to make three different albums
print(make_album('Frost', 'Shut the fuck up', '18'))
print(make_album('Spaghetti', 'Yeet'))
print(make_album('Bob', 'I know nothing about music', '1'))

# ------------------------------------------- #

# Copying the function above, and adding a while loop that gathers 
# input from the user for the album. 

# This exercise melted my brain and kept me from moving on through this book for
# Some reason, so, it kindof works. But not really. Im skipping it anyways fite me.

print('\n')

awnser = True

def make_album_alt(name = '', title = '', numtracks = ''):
	album2 = {'Artist Name': '', 'Album Title': '' }

	'''Adding input'''
	name = input('Who made this album? ')
	title = input('What is the name of this album? ')
	numtracks = input('How many tracks are in this album? ')

	'''Defining the while loop'''
	while awnser == True:
		question = input('Would you like to make another album? (y/n)')

		if question == 'y': 
			awnser == True
		elif question == 'n':
			awnser == False
			break

	'''Adding in optional number of tracks argument'''
	if numtracks:
		album2['numtracks'] = numtracks

	return album2

# Calling the function
print(make_album_alt())

# ------------------------------------------- #



