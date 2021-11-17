# a function can return any kind of value you need it to like lists and dictionaries

def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    return person

athlete = build_person('justin', 'gatlin')
print(athlete)

print("let's try to add extra dimensions to this ")

def build_person(first_name, last_name, age=None): # what does 'none' do that an empty string doesn't?
    """Return a dicitonary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age']= age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)