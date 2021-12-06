favorite_pizza = ['supreme pizza', 'pepperonini pizza', 'jalepeno pizza']
print(favorite_pizza)

friend_pizza = favorite_pizza[:]
friend_pizza.append('italian sausage pizza')

print(friend_pizza)

for pizza in friend_pizza:
    print(f"I guess you do like {pizza}.") #make sure you call on the correct attribute-thingy