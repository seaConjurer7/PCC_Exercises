# A small program working with lists using while loops
# Carsen Weinzetl 03/16/2019

unconfirmed_users = ['Bill', 'Bob', 'Tom']
confirmed_users = []

# Confirming each user, and entering them into the confirmed users list
while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print('Verifying user: ' + current_user.title())
	confirmed_users.append(current_user)

print('\n')

# Printing all the confirmed users 
print('The following users have been confirmed:')
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

print('\n')

# Using a while loop to remove all of a certian item from a list
food = ['Spaghetti', 'Apple', 'Herpes', 'Kumquat', 'Chicken', 'Herpes']
print(food)

print('Yea, lets get rid of the herpes in the food...')
 
while 'Herpes' in food:
	food.remove('Herpes')

print(food)

# Filling a list with user responses
responses = {}

# Making a flag to indicate the polling is active
polling_active = True

while polling_active:
	# Prompting a persons name and response
	name = input('What is your name? ')
	response = input('Which mountian would you like to climb someday? ')

	# Storing the responses
	responses[name] = response

	# Find out if anyone else wants to take the poll
	repeat = input('Would you like to let another person respond? (yes/no)')
	if repeat == 'no':
		polling_active = False

# Polling is complete, show the results
print('\n--- Poll Results ---')
for name, response in responses.items():
	print(name + ' would like to climb ' + response + '.')

