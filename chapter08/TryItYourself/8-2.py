# Write a function called favorite_book() that accepts one parameter, 'title'. The function should print a message, such as 'One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.

def favorite_book(title):
    """This will take an argument(title) the display message"""
    print(f"This is one of my favorite books, {title.title()}")

#favorite_book(Cold Sassy Tree) # error because the argument MUST be in string format
favorite_book('Cold Sassy Tree')