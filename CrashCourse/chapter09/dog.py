class Dog: # class name
    """A simple attempt to model a dog.""" # simple description

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self): #function stored in the class object
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command"""
        print(f"{self.name} rolled over!")

my_dog = Dog('Tuna', 8)

print(f"My dog's name is {my_dog.name}")
print(f"{my_dog.name} is {my_dog.age} years old.")

#I talked a big game about how confusing i found javascript's classes. 

my_dog.sit()
my_dog.roll_over()

print('\n***************************')

your_dog = Dog('Rover', 23)
your_dog.roll_over()