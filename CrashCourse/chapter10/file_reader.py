# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents)

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# let's try to build a single string containing all the digits in the file with no whitespace in it

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = '' # this is an empty string where we want to store pi
for line in lines: 
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string)) # get the character length of the saved file