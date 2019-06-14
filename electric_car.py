# Creating a superclass 
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

		'''Initialize attribute specific to electric cars'''
		self.battery_size = 70

	def describe_battery(self):
		'''Print a description of the cars battery'''
		print('This car has a ' + str(self.battery_size) 
			+ '-kWh battery.')

# Checking to make sure that the inheritence worked 
my_car = ElectricCar('Tesla', 'Model S', 2019)
print(my_car.get_descriptive_name())

# Checking to make sure the subclasses method works
my_car.describe_battery()