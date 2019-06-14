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
