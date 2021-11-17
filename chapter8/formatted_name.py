def get_formatted_name(first_name, last_name): #create function with arguments
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}" #initializing variable to store formatted names
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix') #musician is a variable storing the function
print(musician) # print the function being stored in musician

print('*********************')

def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title() # be aware of your return placement

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)