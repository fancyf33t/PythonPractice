users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

print('*******************************************')

# i want dictionaries nested in dictionaries detailing everyone's second language choice

classmates = {
    'keitron': {
        'first': 'javascript',
        'second': 'python',
        'third': 'c++',
    },
    'lorraine': {
        'first': 'javascript',
        'second': 'python',
        'third': 'none',
    },
    'patrick': {
        'first': 'javascript',
        'second': 'python',
        'third': 'c#',
    },
    'takia': {
        'first': 'javascript',
        'second': 'python',
        'third': 'none',
    },
    'kate': {
        'first': 'javascript',
        'second': 'python',
        'third': 'none',
    },
    'valencia': {
        'first': 'javascript',
        'second': 'php',
        'third': 'moo',
    },
    'jordan': {
        'first': 'javascript',
        'second': 'c#',
        'third': 'python',
    },
}

for classmate, language in classmates.items():
    print(f"\nClassmate: {classmate}")

    learning = f"{language['first']}, {language['second']}, {language['third']}"
print(f"\n{classmate.title()} will be learning {learning}.")
print(f"\n{classmate.title()} shall learn {learning}.")
print(classmate)