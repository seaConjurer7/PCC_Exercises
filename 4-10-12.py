# A small program splicing lists of pizza
# Carsen Weinzetl 03/04/2019

# Making a list for pizza types 
pizzas = ['Cheese', 'Perperroni', 'Lamb', 'Hawaiian', 'Veggie']

# Printing the first three items in the list with a slice
print('The first three items in the list are:\n' + str(pizzas[0:3]))
print("\n")

# Printing the three items in the middle of the list
print('The three items in the middle of the list are:\n' + str(pizzas[1:4]))
print('\n')

# Printing the last three items in the list
print('The last three items in the list are:\n' + str(pizzas[2:7]))
print('\n')


# Making a new list for friends pizzas
f_pizzas = ['Cheese', 'Perperroni', 'Lamb', 'Hawaiian', 'Veggie']

# Inserting one different pizza type to each list
pizzas.insert(0, 'Meatlovers')
f_pizzas.insert(0, 'Six Cheese')

# Proving that the pizzas were put into two seperate lists
print('My pizzas are:\n' + str(pizzas) + '\n')
print('My friends pizzas are:\n' + str(f_pizzas) + '\n')

# Making two for loops to print the lists again
print('My pizzas printed with a for group:')
for pizzas1 in pizzas:
	print(str(pizzas1))
print('\n')

print('My friends pizzas are:')
for f_pizzas1 in f_pizzas:
	print(str(f_pizzas1))
