def describe_pet(animal_type, pet_name): #this uses positional arguments to determine the placement of each argument made in the parameter
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('cat', 'Mr Andeson')
describe_pet('dog', 'Butter') #once the function is made, you can use it multiple times
# be aware that python will run the program regardless of proper argument placement so pay attention!
print('****************************')
print('unless you use keyword arguments')

describe_pet(pet_name='jermaine', animal_type='fish') #keyword arguments allow for proper placement of arguments regardless of position

# if you define a 'default value' for the parameter, 'you can exclude the corresponding argument you'd usually write in the function call. Using default values can simplify your function calls and clarify the ways in which your functions are typically used

# def describe_pet(animal_type='horse', pet_name='tuna'): #this uses positional arguments to determine the placement of each argument made in the parameter
#     """Display information about a pet"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")