# A program containing exercises from chapter 9
# 06.07.2019

# Importing all classes from module
from chap9module import *

# -------------------------------------------------------------------------- #

# 9-2

# Accessing attributes
Chillis = Restaraunt('Chillis', 'Burger')
Whattaburger = Restaraunt('Whattaburger', 'fast food')
Starbucks = Restaraunt('Starbucks', 'breakfast')

# Calling methods
Chillis.describe_restraunt()
Whattaburger.describe_restraunt()
Starbucks.describe_restraunt()


# -------------------------------------------------------------------------- #

# 9-3

# Accessing attributes
me = User('Carsen', 'Weinzetl', 19, 'Green')

# Calling methods
print('\n')
me.describe_user()
me.greet_user()

# -------------------------------------------------------------------------- #

# 9-4 

# Calling new methods that access and modify the attribute 'number_served'
print('\n')
Chillis.set_number_served(20)
Chillis.print_served()

# -------------------------------------------------------------------------- #

# 9-5

# Calling new methods that increase login in attempts, and then reset them
# back to zero
print('\n')

# Three login attempts
me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
me.print_login_attempts()

# Resetting the login count
me.reset_login_attempts()
me.print_login_attempts()

# -------------------------------------------------------------------------- #

# 9-6

# Creating an instance with the subclass IceCreamStand, and calling its method
# for listing flavors that the stand offers
print('\n')

Baskin = IceCreamStand('Baskin', 'Ice Cream')

Baskin.list_flavors()

# -------------------------------------------------------------------------- #

# 9-7

# Calling a method from a subclass of 'User()' that lists the privlages of
# the administrator 
print('\n')

Admin = Admin('Carsen', 'Weinzetl', 19, 'Green')

# Admin.list_privlages()

# -------------------------------------------------------------------------- #

# 9-8

# Creating another class for the admins privlages, and moving the method to
# the new class 'Privlages()'

Admin.privlages.list_privlages()

# -------------------------------------------------------------------------- #

# 9-9

# Creating a method within the 'ElectricCar()' class to upgrade the battery
# inside the vehicle. Then call the get_range() function to show the change
# in range from the new battery
print('\n')

# Declaring vehicle, showing its range, and describing the battery
CarsenEV = ElectricCar('Chevy', 'Volt', 2018)
CarsenEV.battery.get_range()
CarsenEV.battery.describe_battery()

# Using the upgrade battery method, showing the actual change of the battery,
# and improved range
print('\n')

CarsenEV.battery.upgrade_battery()
CarsenEV.battery.get_range()
CarsenEV.battery.describe_battery()

# -------------------------------------------------------------------------- #
