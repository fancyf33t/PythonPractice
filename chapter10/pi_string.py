filename = 'pi_million_digits.txt'

with open(filename) as file_object: # opening txt file
    lines = file_object.readlines()
    pi_string = '' # places within empty string
    for line in lines: # breaks down lines, places in one
        pi_string += line.strip() # removes whitespace


print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ") #displays in terminal of VS
if birthday in pi_string: # if what we type in input =
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi!")

