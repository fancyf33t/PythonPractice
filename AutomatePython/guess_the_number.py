# Write your code here :-)
# This is a guess number game.
import random #this imports the random function from Python libraries
secretNumber = random.randint(1,20) #stores a random number between 1 and 20 inside of the variable secretNumber
print('I am thinking of a number between 1 and 20')

# Ask the player to guess 6 times.
for guessesTaken in range(1,7): #this limits the amount of guesses permitted
    print('Take a guess.')
    guess = int(input()) #input passes values into str by default

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high')
    else: #you don't need an elif here. you need an else
        break #this condition is the correct guess
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of ' + str(secretNumber))
