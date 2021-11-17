# use a for loop to count numbers up to 20

for value in range(1,20):
    print(value)

for value in range(1,30,2):
    print(value)

for value in range(1,30):
    print(value *3)

for square in range(1,11):
    print(square **2)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)
print(friend_foods)

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)


print('****************************')

dimensions = (300, 70)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)