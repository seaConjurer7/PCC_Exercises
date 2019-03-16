# A program practicing using dictionaries
# Carsen Weinzetl 03/05/2019


# Defining a dictionary for alien 0
alien_0 = {'color': 'red', 'points': '5'}

# Printing that a player has earned points for shooting down an alien,
# using the dictionary for said alien
new_points = alien_0['points']
print('You got, ' + str(new_points) + ' points!')

print('\n')

# Adding new key values to the dictionary for the aliens location
print('The original dictionary values:')
print(alien_0)

alien_0['xposition'] = 0
alien_0['yposition'] = 25

# Printing the new dictionary with the added values
print('The new dictionary with added values')
print(alien_0)

print('\n')

# Modifying values of the dictionary
# Changing the aliens color and printing it
# Making it purple
alien_0['color'] = 'Purple'
print('The alien is now, ' + alien_0['color'].lower() + '!')

# Making it yellow
alien_0['color'] = 'Yellow'
print('The alien is now, ' + alien_0['color'].lower() + '!')

print('\n')

# Determining how fast an alien is by tracking its movement 

# Defining and printing the starting x position of the alien
alien_0 = {'xposition': 0, 'yposition': 25, 'speed': 'medium'}
print('Original x position: ' + str(alien_0['xposition']))

# Moving the alien to the right
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

# Defining and printing the new position of the alien
alien_0['xposition'] = alien_0['xposition'] + x_increment
print('New x position: ' + str(alien_0['xposition']))

