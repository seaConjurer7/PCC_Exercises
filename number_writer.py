import json

numbers = [1, 2, 3, 4, 5]

# Writing 'numbers' to the json file
filename = 'numbers.json'
with open(filename, 'w') as fl_obj:
	json.dump(numbers, fl_obj)
	