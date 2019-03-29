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


