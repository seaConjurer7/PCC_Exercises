# Exercise programs from chapter 7 with random themes
# Carsen Weinzetl 03/12/2019

# A loop that takes a users pizza toppings and adds them to their order
que = '\nWhat toppings would you like on your pizza?'
que += '\n(Enter "done" to stop entering toppings)\n\t'
toppings = []

active = True
while active:
	toppings.append(input(que))

	if toppings[-1] == 'done':
		toppings.pop()
		print('OK, so you want the following toppings on your pizza: ' + str(toppings))
		active = False
		continue

print('\n')

# Writing a while loop that will determine the cost of a persons ticket
age = 'Your age will determine how much your ticket is.'
age += '\nEnter your age as a number:\n\t'
cost = input(age)

sale = True
while sale:
	if int(cost) <= 3:
		price = 'FREE'
		print('Your ticket will be ' + str(price) + '!')
		sale = False
		continue

	elif int(cost) >= 3 and int(cost) <= 12:
		price = 10
		print('Your ticket will be ' + str(price) + ' dollars')
		sale = False
		continue

	elif int(cost) >= 15:
		price = 15
		print('Your ticket will be ' + str(price) + ' dollars')
		sale = False
		continue

	elif cost : 
		print('Please enter a numerical value')

#
