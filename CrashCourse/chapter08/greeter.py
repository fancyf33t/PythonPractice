# def greet_user():
#     """Display a simple greeting"""
#     print("Hello!")

# greet_user()

# add a new dimension to the function

def greet_user(username):
    """Display a simple message"""
    print(f"Hello, {username.title()}")

greet_user('keitron')
print('***************************')

# let's start using functions that contain while loops

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

    #this is an infinite loop. explain which line is the problem
# while True: #this never includes a break or a condition to end the program
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}")
while True:
    print('\nPlease tell me your name:')
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
print('**************************************')

def give_vehicle_info(make, model, year):
    """Return vehicle information neatly"""
    vehicle = f"So you are interested in a {year} {make.title()} {model.title()}."
    return vehicle

while True:
    print('\nWhat car do you want?')
    print("(enter 'q' at any time to quit)")

    question1 = input('What is the make?')
    if question1 == 'q':
        break
    question2 = input('What about the year?')
    if question2 == 'q':
        break
    question3 = input('How about the model?')
    if question3 == 'q':
        break
    vehicle_information = give_vehicle_info(question1, question2, question3)
    print(f"{vehicle_information}")
print('**************************')