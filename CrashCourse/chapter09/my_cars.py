from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name()) #i am importing these class and functions from a separate file in python

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# you can import an entire module and then access the class you need using dot notation

import car

my_beetle = car.Car('volkswagen', 'thing', 1953)
print(my_beetle.get_descriptive_name())

favorite_car = my_beetle.get_descriptive_name()

message = f"My favorite car ever is a {favorite_car}."

print(message)