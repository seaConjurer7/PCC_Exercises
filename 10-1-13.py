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

