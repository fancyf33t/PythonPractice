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