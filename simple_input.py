# create a simple input for keyboard
"""
1) Make a program that asks a phone number
2) Make a program that asks for a programming language (add a layer)
"""

question = input("Give me a number between 1 and 10: ")

if int(question) < 1:
    print('that is less than 1, sir or madame')
elif int(question) > 10:
    print('that is too much')
else:
    print(f'Here is your number: {int(question)}')
# great this works