from city_function import get_location

print("Where would you like to go?")
print("Enter 'q' at any time to quit.")
while True:
    city = input("\nGive me a city: ")
    if city == 'q':
        break
    country = input("\nGive me a country: ")
    if country == 'q':
        break

    new_location = get_location(city, country)
    print(f"\tIt looks like you want to go to {new_location}.")