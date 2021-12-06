# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)

# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")


# i want to make an age verification input

age = input("Please enter your age: ")
age = int(age)

if age >= 18:
    print(f"\nYou are good to go!")
else:
    print(f"\nNot today")

from datetime import date
today = date.today()

print(today)