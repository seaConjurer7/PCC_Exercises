# Module for chapter 9 exercises

class Restaraunt():

	def __init__(self, name, cuisine_type):
		self.name = name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restraunt(self): 
		print(self.name.title() + "'s, is a " + self.cuisine_type.title()
			+ ' restaraunt.')

	def set_number_served(self, number_served):
		self.number_served = number_served

	def increment_number_served(self, increment):
		if increment >= 1:
			self.number_served += increment
		else: 
			print('Please enter a positive number.')

	def print_served(self):
		print(str(self.number_served) + ' people served thusfar.') 

class User():

	def __init__(self, first_name, last_name, age, favorite_color):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.favorite_color = favorite_color
		self.login_attempts = 0

	def describe_user(self):
		print('The users full name is, ' + self.first_name.title() 
			+ ' ' + self.last_name.title() + '. They are ' + str(self.age)
			+ ' years old, and their favorite color is ' + self.favorite_color)

	def greet_user(self): 
		print('Hello, ' + self.first_name.title() + '!')

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

	def print_login_attempts(self):
		print(str(self.login_attempts) + ' Login attempts so far.')

