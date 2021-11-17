#store information about a pizza being ordered

pizza = {
    'crust': 'thick', 
    'toppings': ['mushrooms', 'extra cheese'],
}
#storing a list in a dictionary.... use proper python syntax for nesting of the list inside of a dictionary
#summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")