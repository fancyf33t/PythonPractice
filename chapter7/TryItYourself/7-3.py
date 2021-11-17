#ask the user for a number, and then report whether the number is a multiple of 10 or not

number = input("Give me a number and I will see if it is a multiple of 10 or not: ")
number = int(number) #this will prevent any traceback error from not turning an interger into a string?

if number % 10 == 0:
    print(f"\nI guess {number} works")
else:
    print(f"\n{number} doesn't work...")
