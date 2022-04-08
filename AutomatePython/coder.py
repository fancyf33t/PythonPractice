# Write your code here :-)
coders = {'Keitron': 'python' }

while True:
    print('Who all is in attendance today? (type "q" to quit)')
    name = input()
    if name == 'q':
        break

    if name in coders:
        print(coders[name] + ' is already here')
    else:
        ('I do not know who that is... ')
        Print('What is their preferred language?')
        language = input()
        coders[name] = language
        print('Updated')
