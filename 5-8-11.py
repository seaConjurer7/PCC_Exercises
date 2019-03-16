# A program practicing using if statements with lists
# Carsen Weinzetl 03/05/2019


# A program for printing log on messages, and a special message for admins
users = ['admin', 'sudent', 'guest', 'teacher']

for user in users:
	if user == 'admin':
		print('Welcome, ' + str(user.title()) + '. 1 system report qued')
	else: 
		print('Welcome, ' + str(user.title()) + "." )

print('\n')

# Programming output if users is empty, using an if statement
users = []

if len(users) == 0:
	print('No users found.')

print('\n')


# A program that checks to see if a user name has already been taken

# Defining lists for taken usernames, & new usernames pending
current_users = ['Chuck', 'Bob', 'Bill', 'Poe', 'Tim']
new_users = ['Chuck', 'Tom', 'Frank', 'Poe', 'Frost']

# Checking to see if a new_users is already in current_users
for check in new_users:
	if check == current_users[0]:
		print('Sorry, ' + str(check) + " is already taken." + " Please enter another username.")
	elif check == current_users[1]:
		print('Sorry, ' + str(check) + " is already taken." + " Please enter another username.")
	elif check == current_users[2]:
		print('Sorry, ' + str(check) + " is already taken." + " Please enter another username.")
	elif check == current_users[3]:
		print('Sorry, ' + str(check) + " is already taken." + " Please enter another username.")
	elif check == current_users[4]:
		print('Sorry, ' + str(check) + " is already taken." + " Please enter another username.")
	else: 
		print('Username is avalible.')

print('\n')


# A program that checks each number and outputs their ordinal suffix with the number

# List of numbers that need their ordinal suffixes
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Printing a list of number, with their ordinal suffixes:')

# For loop and if-elif-else that checks and prints each ordinal number as a string
for ordinal in numbers:
	if ordinal == 1:
		print(str(ordinal) + "st")
	elif ordinal == 2: 
		print(str(ordinal) + "nd")
	elif ordinal == 3:
		print(str(ordinal) + "rd")
	else:
		print(str(ordinal) + "th")
