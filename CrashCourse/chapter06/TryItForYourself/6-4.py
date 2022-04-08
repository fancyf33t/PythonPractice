glossary = {
    'print': 'produces a final output for your program',
    'dictionary': 'a collection of key-value pairs',
    'comments': 'allow code to be written in the program but not read/interfere with the functionality of the program',
}

print(glossary['print'])
print(glossary['dictionary'])
print(glossary['comments'])

print('************************')

#so i have to actually call out the key:value in my for loop?

for key, value in glossary.items(): #you have to call items() for a key:value dictionary for loop
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")
