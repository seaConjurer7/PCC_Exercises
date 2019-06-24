import json 

# Using the '.load()' function from json to read the json file contents
filename = 'numbers.json'
with open(filename) as fl_obj:
	numbers = json.load(fl_obj)

print(numbers)