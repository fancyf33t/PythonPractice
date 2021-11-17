#Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website....
#if username is 'admin', make a special greeting

username_list = [
    'valencia',
    'lorraine',
    'keitron',
    'patrick',
    'john',
    'admin',
]
name = 'admin'
for name in username_list:
    if name == 'admin':
        print("Why hello, master!")
    elif name == 'lorraine':
        print("It's you. The angel.")
    else:
        print(f"Ugh, {name.capitalize()}. Get the fuck out of here!!")
#this is getting much easier to understand