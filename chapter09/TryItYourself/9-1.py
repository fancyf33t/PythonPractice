# Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods

class Restaurant:
    """A simple try at describing a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initiaize name and cuisine for the restaurant class"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        """welcome message"""
        print(f"{self.restaurant_name} is a restaurant that specializes in {self.cuisine_type} cooking.")\

    def open_restaurant(self):
        """closing message"""
        print(f"{self.restaurant_name} is open for business")


my_restaurant = Restaurant('Keitron\'s Bistro', 'american bistro')

my_restaurant.describe_restaurant()

my_restaurant.open_restaurant()