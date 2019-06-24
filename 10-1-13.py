# Program for writing all exercise programs in chapter 10
# 06.19.2019 Carsen Weinzetl

# -------------------------------------------------------------------------- #

# 10-3

'''
# Taking the users name as a var 'username' & initializing filename
username = input('What is your name? ')
filename = 'guest.txt'

# Adding the users name to the guest list
with open(filename, 'a') as file_object:
	file_object.write(str(username + '\n'))
'''

# -------------------------------------------------------------------------- #

# 10-4 

'''
# Creating a while loop that prompts users for their names,
# creates a greeting, and logs their name in a file 'guest_book.txt'
newpeople = True

while newpeople:

	# Gathering guest name, and generating greeting
	guest = input('What is your name? ')
	greeting = str.title(guest) + ', welcome to the party!'
	print(greeting)

	# Writing guest name to 'guest_book.txt'
	filename = 'guest_book.txt'

	with open(filename, 'a') as file_object:
		file_object.write(str(guest + '\n'))

	# Promting the user if there are anymore guests
	question = input('Are there any more guests to add? (Y/N) ')

	# Checking to see if anyone else needs to be added
	if question == 'n':
		newpeople = False
	elif question == 'y':
		continue
	else:
		print('Please respond either "Y" or "N".')
'''

# -------------------------------------------------------------------------- #

'''
# 10-5

# Creating a while loop that gathers peoples reasons behind liking programming
# , and then stores the reasons in a file 'reasons.txt'
reasons = True

while reasons:

	# Gathering the users 'reason'
	reason = input('Why do you like programming? ')

	# Writing reason to file 'reasons'
	filename = 'reasons.txt'

	with open(filename, 'a') as file_object:
		file_object.write('\n' + reason)

	# Prompting user for additional reasons
	more_reasons = input('Would you like to add more reasons? (y/n) ')

	if more_reasons == 'y':
		continue
	elif more_reasons == 'n':
		reasons = False
	else:
		print('Please respond either "Y" or "N".')
'''

# -------------------------------------------------------------------------- #

# 10-6 

# Creating a program that prompts the user for two inputs to add together
# and if it gets a ValueError, return an error message

# Making a function to find the sum of two numbers
def Sum():
	'''Find the sum of two numbers'''

	try:
		value1 = int(input('Enter a number: '))
		value2 = int(input('Enter a number: '))
		value1 + value2
	except ValueError:
		'''Prompting the user to enter an integer'''
		print('Please enter two integers to add together. ')
		Sum()
	else:
		total = value1 + value2 
		print('The sum of the two numbers is: ' + str(total))

# Calling the function
# Sum()

# -------------------------------------------------------------------------- #

# 10-7

'''
This exercise expected the following exercise to be written alone, and not
as a function. 

It wanted me to then, wrap the former exercises code in a while loop, 
so the user can re enter an integer to try again to find the sum.
However I have implemented the same feature through a function.

... So Im just going to skip this one lmao.
'''

# -------------------------------------------------------------------------- #

# 10-8

# A program that reads from two files, and prints the files contents. 
# The program also will utilize a try block, and use 'except', to return
# an error message if it cannot locate the file. 

# The two files will contain the names of random cats & dogs

def ReturnContents():
	'''Reading the contents of two files and then printing them out'''

	try:
		'''Checking for the two files'''
		filenames = ['cats.txt', 'dogs.txt']

		'''
		Adressing each file, and printing a custom message,
		that also reads the contents of the file
		'''
		for file in filenames: 
			with open(file, 'r') as fl_obj:
				content = fl_obj.read()
				print('The names listed in the file, ' 
					+ str(file.title())
					+ ' are: ' 
					+ str(content.split()))

	except FileNotFoundError:
		print('Could not find the specified files.')

# Calling the function		
# ReturnContents()

# -------------------------------------------------------------------------- #

# 10-9

# This exercise takes the former exercises code and makes the exception
# pass 'silently', you can do this by simply deleting the 'print' error

# -------------------------------------------------------------------------- #

# 10-10

# Creating a program that takes a file and finds how many times
# a specific word shows up, throught the entire file

def WordFinder(file, word):
	'''
	Given a file, and a specific word. This function will find all
	instances of the specific given word. 
	'''

	try: 
		'''Printing a custom statement'''
		with open(file, 'r') as fl_obj:

			words = fl_obj.read()
			number_of_words = words.lower().count(word)
			print('There are, ' 
				+ str(number_of_words)
				+ ' instances of the word: '
				+ word
				+ ', in the file '
				+ file )

	except FileNotFoundError:
		print('File could not be found. ')

	except: 
		print('Something has gone wrong. ')

# Calling the function to check and make sure this works
WordFinder('cats.txt', 'cheese')
WordFinder('frozennorth.txt', 'cold')

# -------------------------------------------------------------------------- #