#write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value

prompt = "\nTell me the ingrdients you want: "
prompt += "\nEnter 'quit' to end the program."

ingredient = ""
while ingredient != 'quit':
    ingredient = input(prompt)

    if ingredient != 'quit':
        print(ingredient)
