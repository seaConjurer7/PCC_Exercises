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
def tshirt(size, message):
	print('\nThe shirt is a size, ' + size.lower() + '. That says: ' + message.title())

# Calling the function
tshirt(
	size = 'Large',
	message = 'Theres no speed limit in heaven.'
)

# ------------------------------------------- #





