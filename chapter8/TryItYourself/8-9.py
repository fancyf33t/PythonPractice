# Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message

def show_messages(messages):
    """this will display messages from my list"""
    for message in messages:
        msg = f"Message: {message}"
        print(msg)

messages = [
    'i',
    'like',
    'bourbon'
]
show_messages(messages)

# ok. i got it to work. i will do this five more times....

def show_names(names):
    """I want to display names on the list"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)
guest_list = [
    'siera',
    'nico',
    'taylor',
    'tiara',
    'rhea',
    'michael'
]
new_list = []
show_names(guest_list, new_list[:])
print(f"\nle'ts try this again...")

# function_name(list_name[:]) let's you send a copy of a list to send the function