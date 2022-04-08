# Start with your program from 3-6.py. 
# Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until onluy two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know your're sorry you can't invite them to dinner
# Print a messge to each of the two people still on your list, letting them know they're still invited
# Use del to remove the last two names from your list, so you can have an empty list.
# Print your list to make sure you actually have an empty list at the end of your program


guest_list = ['paul morphy', 'vera menchik', 'gordon ramsey', 'neil deGrasse tyson', 'siera sepulveda']
more_people = ['levy rozman', 'hikaru nakamura', 'octavia spencer']
new_list = guest_list + more_people
print(new_list)
# now to remove everyone from the list
chopping_block = new_list.pop()
print(chopping_block)
print(new_list)
chopping_block = new_list.pop()
print(chopping_block)
print(new_list)
chopping_block = new_list.pop()
print(chopping_block)
print(new_list)
chopping_block = new_list.pop()
print(chopping_block)
print(new_list)
chopping_block = new_list.pop()
print(chopping_block)
print(new_list)

# now use del statement

del new_list[0]
del new_list[1]
print(new_list)
del new_list[0]
print(new_list) # a bit repetitive but it is done for now