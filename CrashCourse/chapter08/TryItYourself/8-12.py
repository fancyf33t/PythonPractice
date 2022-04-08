# Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that's being ordered. Call the function three times, using a different number of arguments each time

def sandwich_order(bread, *toppings):
    """This function will take on orders for making sandwiches"""
    print(f"\nThey want {bread} bread with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

order_1 = sandwich_order('white', 'lettuce', 'onion', 'tomato')
order_2 = sandwich_order('wheat', 'lettuce', 'olives' )
