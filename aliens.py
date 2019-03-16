# A program practicing new concepts in the 6th chapter
# Carsen Weinzetl 03/06/2019

# Storing multiple dictionaries in a list
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'red', 'points': 10}
alien_2 = {'color': 'yellow', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

# Printing each individual dictionary from the list
for alien in aliens:
	print(alien)

print('\n')

# Making a list with 30 dictionaries of aliens, that are generated automatically

# Emptying the list
aliens = []

# Making 30 aliens with a for loop
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5}
	aliens.append(new_alien)

# Changing the first three aliens dictionary color and points
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = '10'

# Printing the first five aliens
for alien in aliens[:5]:
	print(alien)

print('\n')

# Checking to make sure 30 aliens got made
print('Total number of aliens is: ' + str(len(aliens)))
