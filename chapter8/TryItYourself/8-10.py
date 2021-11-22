# Start with a copy of your program from 8-9.py. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it's printed. After calling the function, print both of your lists to make sure the messages ere moveed correctly

def show_names(names, sent_messages):
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
def messages_to_send(sent_messages):
    """This SHOULD copy down anything that has been sent by the first function"""
    print("\nThe following has been sent:")
    for sent_message in sent_messages:
        print(sent_message)

sent_messages = []
show_names(guest_list, sent_messages)
messages_to_send(sent_messages)
print(sent_messages)