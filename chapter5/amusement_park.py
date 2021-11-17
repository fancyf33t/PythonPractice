age = 12
age = 19
if age < 4:
    print("Your admission cost is $0.")
elif age < 18: #with elif, the stored information in the variable does not exceed the parameter set in the if-elif-else statement
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

print("***********************************")

age = 35

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
    print("Full price for you.")
print(f"Your admission price is ${price}.")

print("*****************************************")

#just move them around. you understand what is happening
age = 18
age = 70
age = 3
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else: #"Python does not require an else block at the end of an if-elif chain. Use it for the sake of clarity"
    price = 20
print(f"Your admission cost is ${price}.")

print("**************************************")

