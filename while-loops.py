# A small program practicing different concepts with while loops
# Carsen Weinzetl 03/12/2019

# Using a while loop to count to 5 and then stop
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

# Program where the user chooses when to quit using a while loop
prompt = '\nTell me something, and I will repeat it back:'
prompt += '\nEnter "quit" to end the program\n\t'

active = True
while active: 
	message = input(prompt)

	if message == 'quit':
		active = False
	else: 
		print(message)

# Using break to exit a loop
prompt2 = '\nPlease enter the name of a city you have visited:'
prompt2 += '\n(Enter "quit" when you are finished.)\n\t'

while True:
	city = input(prompt2)

	if city == 'quit':
		break
	else: 
		print("I'd love to go to " + city.title() + "!")

# Using 'continue' to stop a loop, but not quite the entire program
# This program prints odd numbers with a while loop, using continue
# if parameters are not met
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue 

	print(current_number)

# 