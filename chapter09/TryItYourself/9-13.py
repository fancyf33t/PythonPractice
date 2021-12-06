# Make a class Die with one attribute called sides, which has a default value of 6. 
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has.
# Make a 6-sided die and roll it 10 times

class Die:
    """I want to make a function that randomizes numbers like a die"""

    def __init__(self, sides):
        """initializes the die"""
        self.sides = 6

    def roll_die(self):
        """this should roll the die"""
        from random import randint
        print(randint(1,6))

my_roll = Die(6)
my_roll.roll_die()
# success. still going to need to practice

