# Write your code here :-)
import random #this imports the random function from python

messages = [ #this list stores the potential responses
    'it is decidedly so',
    'yes definitely',
    'reply hazy try again',
    'ask again later',
    'concentrate and ask again',
    'my reply is no',
    'outlook not so good',
    'very doubtful'
]
print(messages[random.randint(0, len(messages) - 1)])
