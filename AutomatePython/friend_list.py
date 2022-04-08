# Write your code here :-)
friends = []

while True:
    """i want this to push the friend input into the friends list"""
    print("Who do you care most about in this world?")
    name = input() # this is just an empty input box??
    if name == 'quit':
        break
    friends = friends + [name] # this concatonates the list
print(f"Here are your friends: {friends}")
