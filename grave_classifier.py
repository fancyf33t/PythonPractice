# i want to make a program that classifies types of graveyards

# cemetery : a burial ground *not a place of honor
# mausoleum : a large tomb /especially : a usually stone building with places for entombment of the dead above ground
# cenotaph : a tomb or a monument erected in honor of a person or group of persons whose remains are elsewhere
# memorial : serving to preserve remembrance

# make a prompt 
# make an input
    # what do you want to know?
    # ask persons buried
    # attatched to church
# resting_place = 'underground'
# if resting_place == 'empty':
#     print('That does not answer my question')
# elif resting_place == 'special':
#     print('that is a memorial')
# elif resting_place == 'underground':
#     print('that is a catacomb')
# else:
#     print('i don\'t know')
# ok so that works. now i need to add input functions

prompt = "\nTell me about your resting place"
prompt += "\nEnter 'quit' to end the program: "

resting_place = ""
while resting_place != 'quit':
    resting_place = input(prompt)

    if resting_place == 'empty':
        print('cenotaph')
    elif resting_place == 'special':
        print('that is a memorial')
    elif resting_place == 'underground':
        print('that is a catacomb')
    elif resting_place == 'quit':
        break
    else:
        print('i don\'t know')