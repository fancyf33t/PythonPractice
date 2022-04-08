# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.
#   Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments

def make_shirt(message='I love python', slogan="If it doesn't fit, make it!"):
    """This will print a message on the shirt"""
    print(f"The message on the shirt is this: {message}")
    print(f"The slogan is this: {slogan}")

make_shirt() # this should call the default arguments
print('**********************************')
make_shirt('I guess C is cool') # I am only changing the message, not the slogan
print('****************************')
make_shirt(slogan='Definitely love Python')
# it just makes so much sense. i see no reason why other languages are used