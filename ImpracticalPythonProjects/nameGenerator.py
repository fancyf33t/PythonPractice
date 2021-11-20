# Randomly generate sidekick names using Python

# Load a list of first names
# Load a list of surnames
# Choose a first name at random
# Assign the name to a variable
# Choose a surname at random
# Assign the name to a variable
# Print the names to the screen in order an din red font
# Ask the user to quit or play again
# If user plays again => repeat
# If user quits => end and exit

import sys, random
print("Welcome to the Psych 'Sidekick Name Picker.' \n")
print("A name just like Sean would pick for Gus:\n\n")

first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'", 'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield', 'Chewy', 'Chigger', '"Mr Peabody"') # what is the benefit of using tuples??

last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom', 'Fewhairs', 'Hooperbag', 'Jenkins', 'Jingley-Schmidt')

while True: # using while true tells the program to keep running until told to stop. 
    firstName = random.choice(first) # importing random function seems much more efficient that Math.ceil(Math.random()*.length) that I would be forced to do in JS

    lastName = random.choice(last)

    print("\n\n")
    print("{} {}".format(firstName, lastName), file=sys.stderr)
    print("\n\n")

    try_again = input("\n\nTry again? (Press Enter else n to quit)\n")
    if try_again.lower() == "n": # assign the break to end the program
        break
input("\nPress Enter to exit.")
