def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'bell peppers', 'jalepenos')

print('*****************************************')

def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print("\nMaking a pizza with the following topphings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('anchovy', 'mushrooms', 'olives')

print('*****************************************')

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoini')
make_pizza(12, 'veggie', 'anchovy')