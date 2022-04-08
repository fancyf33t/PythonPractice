def build_profile(first, last, **user_info): #pay attention to arbitrary positional arguments
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

print('***********************************')

def friend_information(first, last, **name_info):
    """This is additional practice for functions"""
    name_info['first_name'] = first
    name_info['last_name'] = last
    return name_info
friend = friend_information('siera', 'sepulveda', middle_name='marie', occupation='teacher')
print(friend)