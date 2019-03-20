# Programs for the exercises in chapter seven
# Carsen Weinzetl 03.16.2019

# Making a psuedo restaraunt program that takes orders and makes any kind of food

# Making a dictionary to store all the orders
orders = {}

# Making the flag to continue taking orders
line = True

while line: 
	name = input('\nWhat is the name for the order? ')
	order = input('What would you like? ')

	# Deleting any orders of 'Spaghetti', as we have run out of it sadly
	if order == 'Spaghetti':
		print('Sorry, we have run out of spaghetti.')
		order = input('What else can I get for you? ')

	# Storing the order in the orders 
	orders[name] = order

	# See if anyone else wants to put an order in 
	repeat = input('Are you putting in any other orders? (yes/no) ')

	if repeat == 'no':
			line = False

# Printing all the finished orders
print('\n-- Orders --')
for name, order in orders.items():
			print('Ok, ' + name + ' you had the ' + order)


# Making a program that asks people what their dream vacation would be
# And then printing it back to them using while loops, flags, and
# A dictionary.
vacation = {}

# Making a flag to control the polling
polling_active = True

while polling_active:
	person = input('\nWhat is your name? ')
	vacay = input('What would your dream vacation be? ')

	# Storing the persons vacay in the dictionary
	vacation[person] = vacay

	# Asking if there are any other people who would like to awnser
	again = input('Would you like to add another persons dream vacation? (yes/no) ')

	if again == 'no':
		polling_active = False

# Printing each persons dream vacations
print('\n-- Each persons dream vacation --')
for person, vacay in vacation.items(): 
	print(person + "'s dream vacation is, " + vacay + '.')