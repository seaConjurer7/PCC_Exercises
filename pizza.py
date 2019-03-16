# A small program practicing using dictionaries and lists together to store info
# Carsen Weinzetl 03/06/2019

# Defining an custom pizza order
pizza = {
	'crust': 'stuffed',
	'toppings': ['mushrooms', 'pineapple', 'tomatoes']
}

# Summarising the order
print('You ordered a ' + str(pizza['crust']) + '-crust pizza.' +
	' With the following toppings:')

# Listing all toppings on the pizza
for topping in pizza['toppings']:
	print('\t' + topping.title())