# Module for chapter 9 exercises

class Restaraunt():

	def __init__(self, name, cuisine_type):
		self.name = name
		self.cuisine_type = cuisine_type

	def describe_restraunt(self): 
		print(self.name.title() + "'s, is a " + self.cuisine_type.title()
			+ ' restaraunt.')

class User():

	def __init__(self, first_name, last_name, age, favorite_color):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.favorite_color = favorite_color

	def describe_user(self):
		print('The users full name is, ' + self.first_name.title() 
			+ ' ' + self.last_name.title() + '. They are ' + str(self.age)
			+ ' years old, and their favorite color is ' + self.favorite_color)

	def greet_user(self): 
		print('Hello, ' + self.first_name.title() + '!')

