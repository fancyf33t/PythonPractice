# Write your code here :-)
# make a student name checker using a while loop
# make use of lists first

students_present = [] # this is an empty list to store the names

while True:
    print("Enter the name of the student (or enter 'q' to stop the program)")
    # next is the input for the student names
    name = input()
    if name == 'q':
        break
    # place names inside of list
    students_present = students_present + [name]
# use a for loop to cycle through the stored names
print('These are the students present')
print('+======================+')
for name in students_present:
    print(f'-' + name)
