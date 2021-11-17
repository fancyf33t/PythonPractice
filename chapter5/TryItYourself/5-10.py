current_users = [
    'keitron',
    'takia',
    'lorraine',
    'john',
    'katelyn',
    'michael',
    'jordan',
    'valencia',
]
new_users = [
    'siera',
    'taylor',
    'keitron',
    'nico',
]

for name in new_users:
    if name in current_users:
        print(f"{name.title()}, you are already on the list.")
    else:
        print(f"{name.title()}, you need to make an account.")


best_ever = ['elizabeth', 'jourdan', 'rachel', 'ruwth']
passable = ['her', 'jamie', 'cus']

for name in passable:
    if name in passable:
        print(f"{name.title()}, you need to work on your game.")
    else:
        print(f"well done")