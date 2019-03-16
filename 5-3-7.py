# Making a small program that racks up points for certian colors of aliens you shoot
# Carsen Weiznetl 03/05/2019

# Defining variables for alien color and score
alien = 'Red'
score = 0

# Assigning the points for each color of alien 
if alien == 'Green':
	score = score + 5
elif alien == 'Yellow':
	score = score + 10
elif alien == 'Red':
	score = score + 20

# Printing final score
print(str(score))

print('\n')


# A program determining what stage of life a person is
age = 24

if age < 2:
	stage = 'baby'
elif age > 2 and age < 4:
	stage = 'toddler'
elif age > 4 and age < 13: 
	stage = 'kid'
elif age > 13 and age < 20: 
	stage = 'teenager'
elif age > 20 and age < 65:
	stage = 'adult'
elif age > 65:
	stage = 'elder'

# Printing the stage of life and making sure the statement is gramatically correct
if stage == 'adult' or stage == 'elder':
	print('You are an ' + str(stage) + "!")
else:
	print('You are a ' + str(stage) + "!")

print('\n')


# A program using if statements with lists to find your favorite fruits
fruits = ['Bannanas', 'Kiwi', 'Starfruit', 'Spaghetti']

print('What are some of my favorite fruits?')

if fruits[3] == 'Spaghetti':
	print('You really like Spaghetti!')
if fruits[0] == 'Bannanas':
	print('You really like Bannanas!')
if fruits[1] == 'Kiwi':
	print('You really like Kiwi!')
if fruits[2] == 'Kombucha':
	print('You really like Kombucha!')