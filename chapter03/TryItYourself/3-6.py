# Someone from your list can't attend the party.
# Start with your program from 3-4.py or 3-5.py
# Add a print() call to the end of your program informing people that you found a bigger dinner table
# Use insert() to add one new guest to the beginning of your list
# Use insert() to add one new guest to the middle of yor list
# Use append() to add one new guest to the end of your list
# Print a new set of invitation messages, one for each person on your list (WHY????)

# add three more people. i really don't have that many people i enjoy
guest_list = ['paul morphy', 'vera menchik', 'gordon ramsey', 'neil deGrasse tyson', 'siera sepulveda']
more_people = ['levy rozman', 'hikaru nakamura', 'octavia spencer']
print(f"I am just too popular apparently. It looks like {more_people[2].title()}, {more_people[0].title()}, and {more_people[1].title()} all want to attend this party.")
print(more_people)

new_guest = more_people.pop()
guest_list.append(new_guest)
print(guest_list)

#and so on and so forth...