# Write your code here :-)
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4', 'Davin': 'Sept 19'}

while True:
    print('Enter a name: (black to quit)')
    name = input() #takes the input of the user
    if name == '':
        break #this will end the program

    if name in birthdays: #if the name typed in the input is within the dictionary...
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
