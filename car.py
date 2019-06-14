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
		print('This car has ' + str(self.odometer_reading) + ' miles on it.')

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

# Accessing atributes
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# Modifying the odometer with the method update_odometer
my_new_car.update_odometer(23)
my_new_car.read_odometer()

# Modifying the odometer with the method increment_odometer
my_new_car.increment_odometer(20)
my_new_car.read_odometer()
