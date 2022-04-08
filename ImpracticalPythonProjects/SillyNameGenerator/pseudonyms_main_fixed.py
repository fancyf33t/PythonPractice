# create a silly name generator
# use random, sys, while true, input, and break

import sys
import random


def main():
    """Choose names at random from two lists."""
    print('hello hello')
    print('What name do you get for the rest of your life: ')

    first_name = [
    "3D Waffle", "Hightower", "Papa Smurf", "57 Pixels", "Hog Butcher", "Pepper Legs", "101", "Houston", "Pinball Wizard", "Accidental Genius", "Hyper", "Pluto", "Alpha", "Jester", "Pogue", "Airport Hobo", "Jigsaw", "Prometheus", "Bearded Angler", "Joker's Grin", "Psycho Thinker", "Beetle King", "Judge", "Pusher", "Bitmap", "Junkyard Dog", "Riff Raff", "Blister", "K-9", "Roadblock", "Bowie", "Keystone", "Rooster", "Bowler", "Kickstart", "Sandbox", "Breadmaker", "Kill Switch", "Scrapper", "Broomspun", "Kingfisher", "Screwtape", "Buckshot", "Kitchen", "Sexual Chocolate"
]
    last_name = [
    "Bugger", "Knuckles", "Shadow Chaser", "Cabbie", "Lady Killer", "Sherwood Gladiator", "Candy Butcher", "Liquid Science", "Shooter", "Capital F", "Little Cobra", "Sidewalk Enforcer", "Captain Peroxide", "Little General", "Skull Crusher", "Celtic Charger", "Lord Nikon", "Sky Bully", "Cereal Killer", "Lord Pistachio", "Slow Trot", "Chicago Blackout", "Mad Irishman", "Snake Eyes", "Chocolate Thunder", "Mad Jack", "Snow Hound", "Chuckles", "Mad Rascal", "Sofa King", "Commando", "Manimal", "Speedwell", "Cool Whip", "Marbles", "Spider Fuji", "Cosmo", "Married Man", "Springheel Jack", "Crash Override", "Marshmallow", "Squatch", "Crash Test", "Mental", "Stacker of Wheat", "Crazy Eights", "Mercury Reborn", "Sugar Man", "Criss Cross", "Midas", "Suicide Jockey", "Cross Thread", "Midnight Rambler", "Swampmasher"
]

    while True:
        first = random.choice(first_name)
        last = random.choice(last_name)

        print("{} {}".format(first, last), file=sys.stderr)

        try_again = input("\n\nTry again? (Press 'x' to quit)")
        if try_again == 'x':
            break
        input("cool")
        
if __name__== "__main__":
    main()
