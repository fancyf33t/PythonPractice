# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.)"

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else: 
#         print(f"I'd love to go to {city.title()}!")

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True: #create a while statement then proceed to detail the conditions below
    city = input(prompt) #using input to display the initailized variable (prompt)

    if city == 'quit': #runs the program over and over again until the string 'quit' is typed into the input
        break
    else:
        print(f"I'd love to go to {city.title()}!") #prints the typed in words and capitalizes 

# it works just fine. how do i incorporate this into tkinter?
import Tkinter.Tk()
top.mainloop()