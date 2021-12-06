# this class will store information about the kind of car i am working on
# it will have methods to summarize the info

class Car:
    """A simple attempt to represent a car"""
    
    def __init__(self, make, model, year):
        """initialize attributes to describe a car"""
        self.make = make
        self.model = model 
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())

"""SETTING DEFAULT VALUE FOR ATTRIBUTES

attributes can be defined witout being passed in as parameters. just define the attributes in __init__"""

class Car:
    """A simple attempt to represent a car"""
    
    def __init__(self, make, model, year):
        """initialize attributes to describe a car"""
        self.make = make
        self.model = model 
        self.year = year
        self.odometer_reading = 0 # i will set this as a default value

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# print('\nLet\'s add some miles to it now...')
# second_car = Car('chevorlet', 'trailblazer', 2004)
# second_car.odometer_reading = 4800
# print(second_car.get_descriptive_name())
# second_car.read_odometer()

# """MODIFYING AN ATTRIBUT'S VALUE THROUGH A METHOD

# instead of accessing the attribute directly, try passing the new value to a method that handles the updating internally"""

# class Car:
#     """A simple attempt to represent a car"""
    
#     def __init__(self, make, model, year):
#         """initialize attributes to describe a car"""
#         self.make = make
#         self.model = model 
#         self.year = year
#         self.odometer_reading = 0 # i will set this as a default value

#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         """Print a statement showing the car's mileage"""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     # updating class
#     def update_odometer(self, mileage):
#         """Set th odometer reading to the given value."""
#         self.odometer_reading = mileage

# second_car.update_odometer(23)
# second_car.read_odometer()

"""Incrementing an Attribute's Value Through a Method"""

class Car:
    """A simple attempt to represent a car"""
    
    def __init__(self, make, model, year):
        """initialize attributes to describe a car"""
        self.make = make
        self.model = model 
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value"""
        self.odometer_reading = mileage

# my_new_car = Car('honda', 'civic', 2012)
# print(my_new_car.get_descriptive_name())



class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()