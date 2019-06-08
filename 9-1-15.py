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


