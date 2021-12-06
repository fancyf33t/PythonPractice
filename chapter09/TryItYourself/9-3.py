# Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile.
# Make a method called describe_user() that prints a summary of the user's information. Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user

class Users:
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

student = Users('keitron', 'wallace', 'fancyf33t', 'python')
student2 = Users('james', 'bennet', 'doaaofi', 'javascript')

print('\n**************************')

print(student.greet_user())
print(student2.describe_user())
print(student2.greet_user())