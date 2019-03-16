# A small program to do the excersises for chapter 7
# Carsen Weinzetl 03/10/2019

# Rental car prorgam
rental = input('What make are you intrested in renting?\n\t')

print('OK, lets see if we have a ' + rental + ' avalible for rental!\n')

# Restraunt seating program 
guests = input('How many people are in your party?\n\t')
guests = int(guests)

if guests > 8:
	print('There will be a slight wait for your table.')
elif guests < 8:
	print('OK, right this way!')
else: 
	print('Im sorry how many?')

# Multiple of 10 checker
ten = input('Which number would you like to check?\n\t')
ten = int(ten)

if ten % 10 == 0:
	print(str(ten) + ', is a multiple of 10!')
else:
	print(str(ten) + ', is not a multiple of 10!')
