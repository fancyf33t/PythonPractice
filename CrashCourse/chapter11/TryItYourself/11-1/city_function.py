# Write a function that accepts two parameters: a city name and a country name.
# The function should return a single string of the form City, COuntry
# Store the function in a module called city_function

def get_location(city, country):
    """This function takes a city and a country then combines"""
    location = f"{city}, {country}"
    return location.title()
