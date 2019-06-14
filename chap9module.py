# Module for chapter 9 exercises

class Restaraunt():

	def __init__(self, name, cuisine_type):
		self.name = name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restraunt(self): 
		print(self.name.title() 
			+ "'s, is a " 
			+ self.cuisine_type.title()
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

# a subclass of 'Restaraunt'
class IceCreamStand(Restaraunt):

	def __init__(self, name, cuisine_type):
		super().__init__(name, cuisine_type)

		self.flavors = [
		'Vanilla',
		'Chocolate',
		'Strawberry'
		]

	def list_flavors(self):
		message = 'The following flavors are avalible: '
		message += str(self.flavors) + '.'
		print(message)

class User():

	def __init__(self, first_name, last_name, age, favorite_color):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.favorite_color = favorite_color
		self.login_attempts = 0

	def describe_user(self):
		print('The users full name is, ' 
			+ self.first_name.title() 
			+ ' ' + self.last_name.title() + '. They are ' 
			+ str(self.age)
			+ ' years old, and their favorite color is ' 
			+ self.favorite_color)

	def greet_user(self): 
		print('Hello, ' + self.first_name.title() + '!')

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

	def print_login_attempts(self):
		print(str(self.login_attempts) + ' Login attempts so far.')

# a subclass of 'User()'
class Admin(User):

	def __init__(self, first_name, last_name, age, favorite_color):
		super().__init__(first_name, last_name, age, favorite_color)

		self.privlages = Privlages()

# reallocating a portion of the 'Admin()' class 
class Privlages():

	def __init__(self):
		# Defining admin privlages
		self.privlages = [
		'Ban',
		'Mute',
		'Delete'
		]

	def list_privlages(self):
		# Printing a statement listing the admins privlages
		print('This admin has the following privlages: '
			+ str(self.privlages)
			+ '.')

class Car():
	'''A class to represent a car'''

	def __init__(self, make, model, year):
		self.make = make
		self.model = model 
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		'''Print a statement showing the car's mileage'''
		print('This car has ' + str(self.odometer_reading) 
			+ ' miles on it.')

	def update_odometer(self, milage):
		'''
		Set the odometer to a given value.
		Reject the change if it attempts to roll the odometer back.
		'''
		if milage >= self.odometer_reading:
			self.odometer_reading = milage
		else:
			print('You cannot roll back an odometer.')

	def increment_odometer(self, miles):
		'''Add the given ammount the the odometer'''
		self.odometer_reading += miles

# Creating a subclass from the superclass 'Car()'
class ElectricCar(Car):
	'''Represents aspects of a car, specific to electric vehicles.'''

	def __init__(self, make, model, year):
		'''Initialize attributes of the parent class'''
		super().__init__(make, model, year)

		self.battery = Battery()

	def fill_gas_tank(self):
		'''Print a message to show that there is no gas tank'''
		print('This car has no gas tank!')

# Splitting the 'ElectricCar()' class attribute up into its own class
# to better organise the program 
class Battery():
	'''A simple attempt to model a battery for an electric car'''

	def __init__(self, battery_size=70):
		'''Initialize batterys attributes'''
		self.battery_size = battery_size

	def describe_battery(self):
		'''Print a description of the cars battery'''
		print('This car has a ' + str(self.battery_size) 
			+ '-kWh battery.')

	def upgrade_battery(self):
		'''Change the battery of any car to 85'''
		if self.battery_size == 70:
			self.battery_size = 85
		else:
			print('This cars battery is fully upgraded!')

	def get_range(self):
		'''Print a statement about the batteries range'''
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = 'This car can go approximately ' + str(range)
		message += ' miles on a full charge.'
		print(message)