# Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such a s Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least of which is not in the default country

def describe_city(city, country='America'):
    """Print a message for the city and country"""
    print(f"\n{city.title()} is located in {country.title()}")

describe_city('atlanta')
describe_city('kansas city')

# done. will try adding more dimensions later