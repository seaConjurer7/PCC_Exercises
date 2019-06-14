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

    def get_range(self):
        '''Print a statement about the batteries range'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = 'This car can go approximately ' + str(range)
        message += ' miles on a full charge.'
        print(message)

# Checking to make sure that the inheritence worked
my_car = ElectricCar('Tesla', 'Model S', 2019)
print(my_car.get_descriptive_name())

# Calling methods from a different class
my_car.battery.describe_battery()
my_car.battery.get_range()
