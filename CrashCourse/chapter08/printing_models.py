# Start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# simulate printing each design, until none are left
# move each design to completed_models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

print(f"If this works properly, the unprinted designs should have an empty list: {unprinted_designs}")

# this works. using while and for loops, i can remove information from one list then place them in another

print('\n*******************************')

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing
    """
    while unprinted_designs: #while the list contains items in unprinted_designs
        current_design = unprinted_designs.pop() # takes items and removes them from unprinted designs
        print(f"Printing model: {current_design}")
        completed_models.append(current_design) # append temporarily holds popped items and places them elsewhere

def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron'] # list containing items i want to remove
completed_models = [] # an empty list i want to place items removed from unprinted_designs

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print('did it work??')

print(unprinted_designs)
print('yes it did')

# i will need to practice this over and over until i am comfortable
