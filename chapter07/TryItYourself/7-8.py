#make a list of sandwiches that go into a list of ordered sandwiches

sandwich_orders = ['cold cut', 'italian', 'club', 'reuben', 'club']
finished_orders = []

while sandwich_orders:
    finished_orders = sandwich_orders.pop()
    print("Order up...")
    finished_orders.append('sandwich_orders')
print(finished_orders)
