# Add an attribute called login_attempts to your User class from 9-3.py
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
# Write another method called reset_login_attempts() that resets the value of login_attemps to 0.
# Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
# Print longin_attempts again to make sure it was rest to 0.

class Users: #copied from 9-3
    """Describe users and print messages to the users"""

    def __init__(self, first_name, last_name, username, language):
        """initialize Users class attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language = language

    def describe_user(self):
        """this function will describe the user"""
        print(f"{self.first_name.title()} {self.last_name.title()} logged in with the username {self.username}")

    def greet_user(self):
        """this will send a message to the user"""
        if self.language == 'javascript': # i want to make this function only work with certain conditions.... how can i fix this?
            print(f"Get the hell out of here {self.username} with that {self.language} nonsense!!")
        else:
            print(f"Welcome to the party {self.username}") # you dummy.... you misspelled username
    
    def increment_login_attempts(self):
        """this will keep track of the login attempts"""