# A small program to practice using user inputs and while loops
# Carsen Weinzetl 03/11/2019

# Prompting the user for an input and then printing that input
message = input('Tell me something, and I will repeat it: \n')
print(message)

print('\n')

# Taking input and creating a custom message with it
prompt = 'If you enter your name, your message will be personalized.'
prompt += '\nWhat is your name? \n\t' 

name = input(prompt)
print('Hello, ' + name + '!')

print('\n')

# Turning a string intput into an integer
age = input('What is your age, ' + name + '? \n\t')
age = int(age)

if age > 18:
	print(name + ", you're old enough!" )
else:
	print('Error, you either did not enter a numerical value, or you are too young')

print('\n')

# Rollercoaster ride height check
height = input('How tall are you, ' + name + '? ( in inches )\n\t')
height = int(height)

if height < 36:
	print('You are not tall enough to ride!')
elif height > 36:
	print('You are tall enough to ride! Hop on!')
else: 
	print('Please enter a numerical value')

# Determining if a number is even or odd
evenodd = input('Enter a number to determine if it is even or odd: \n\t')
evenodd = int(evenodd)

if evenodd % 2 == 0:
	print(str(evenodd) + ', is an even number.')
else:
	print(str(evenodd) + ', is an odd number.')