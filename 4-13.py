# A small program practicing using tuples with a buffet theme
# Carsen Weinzetl 03/04/2019 

# Making the tuple of five foods from the buffet
food = ('Rice', 'Beans', 'Shrimp', 'Chicken', 'Steak')

# Printing each item with a for loop
print('The food items in the tuple are:')
for foods in food:
	print(str(foods))
print('\n')

# Changing the tuples values and then printing the list again with a for loop
food = ('Rice', 'Pork', 'Shrimp', 'Spaghetti', 'Steak')

print('The food items in the modified tuple are:')
for foods in food:
	print(str(foods))