

requested_toppings = ['mushrooms', 'extra anchovies']

if 'mushrooms' in requested_toppings:
    print("adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra chesse' in requested_toppings:
    print("Adding extra anchovies.")


print("\nFinished making your pizza!")

print('*****************************')

requested_toppings = ['mushrooms', 'anchovies', 'pepperoni', 'green peppers']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print('\nFinished making your pizza!')

print('**************************')

for requested_topping in requested_toppings: #making a repeating for loop to test if a particular item is within the requested_toppings list
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers at the moment.")
    else: 
        print(f"Adding {requested_topping}")
print("\nFinished making your pizza!!")

print('***************************************')

available_toppings = ['pepperoni', 'spinach', 'ham', 'mushrooms', 'basil', 'olives']
requested_toppings = ['pepperoni', 'spinach', 'feta cheese', 'pineapple', 'pickles']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"No way dude")
    if requested_topping == 'pineapple':
        print(f"{requested_topping.capitalize()}? What the fuck is wrong with you????")
print("\nFinished making your pizza!")