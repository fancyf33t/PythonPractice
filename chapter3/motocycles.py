# To change an element, use the name of the list followed by the index o the element you want to change, and then provide the new value you want that item to have

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# The simplest way to add a new element to a list is to append the item to the list. When you append an item to a list, the new element is added to the end of the list.
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles) # see?

# You can add a new element at any position in your list by using the insert() method
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(1, 'ducati')
print(motorcycles) # this works too

# If you know the position of the item you want to remove from a list, you can use the del statement

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[2]
print(motorcycles)

# You can remove an item from a list by using the pop() method. This allows you to keep working with that item once removed.
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycles = motorcycles.pop()
print(popped_motorcycles) # lovely stuff

# If you only know the value of the item, you can use the remove() method to remove an item without indexing.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('yamaha') #great stuff
print(motorcycles)

