# Start with your program from 3-4.py.
# Add a print() call at the end of your program stating the name of the guest who can't attend
# Modify your list, preplacing the name of the guest who can't make it with the name of the new person you are inviting
# Print a second set of invitation messages, one for each person who is still in your list

guest_list = ['paul morphy', 'vera menchik', 'gordon ramsey', 'neil deGrasse tyson', 'siera sepulveda']

message = f"I would like to thank the following for attending my dinner party: {guest_list}"
print(message)
print(f"\nUnfortunately, {guest_list[2].title()} cannot attend.")

guest_list.remove('gordon ramsey')
guest_list.append('hikaru nakamura')
print(guest_list)

invitation = f"\nThis goes to {guest_list[0].title()}."
invitation2 = f"\nThis goes to {guest_list[1].title()}"
invitation3 = f"\nThis goes to {guest_list[2].title()}."
invitation4 = f"\nThis goes to {guest_list[3].title()}."
invitation5 = f"\nThis goes to {guest_list[4].title()}."

print(invitation, invitation2, invitation3, invitation4, invitation5)

