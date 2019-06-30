# Final exercises for 'Part 1 - Baisics'

# -------------------------------------------------------------------------- #

# 11-1 & 11-2

# Creating a function, and then testing said function by importing 'unittest'
import unittest


def City_Country(city, country, population=''):
    '''Function that returns a detailed statement of a city'''

    if population:
        statement = (
            city
            + ', is in '
            + country
            + '. It has a population of '
            + str(population)
            + ' people!'
        )
    else:
        statement = (
            city
            + ', is in '
            + country
            + '.'
        )

    print(statement)

# Calling the function
# City_Country('Manhattan', 'USA', 1665000)
# City_Country('Manhattan', 'USA')


# Creating a class to test multiple cases of the function 'City_Country()'
class CityCountryTest(unittest.TestCase):
    '''Tests for City_Country()'''

    def test_city_country(self):
        '''Testing function with only the two positional arguments'''
        city_country = City_Country('Manhattan', 'USA')
        self.assertEqual(city_country, 
        	'Manhattan, is in USA.')

    def test_city_country_pop(self):
        '''Testing function with optional argument included'''
        city_country = City_Country('Manhattan', 'USA', 1665000)
        self.assertEqual(city_country, 
        	'Manhattan, is in USA. It has a population of 1665000 people!')

# Calling the test functions
#unittest.main()

# -------------------------------------------------------------------------- #

# 11-3 

# 