cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #sort() method changes the order of the list permanently into alphabetical order.
print(cars) #there is no reversal(i mean that you can't undo the sort)

#unless you reverse sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

"""SORTING A LIST TEMPORARILY WITH SORTED() FUNCTION"""
#to maintain the original order of a list but present it in a sorted order, you can use the sorted() function.
#this allows you to display your list in a particular order but doesn't affect the actual order of the list

cars = ['bmw', 'audi', 'toyota', 'subaru', 'honda', 'mazda', 'ford']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#NOTE: Sorting a list alphabetically is a bit more complicated when all the values are not in lowercase. There are several ways to interpret capital letters when determining a sort order, and specifying the exact order can be more complex than we want to deal with at this time. However, most approaches to sorting will build directly on what you learned in this section

"""Printing a list in reverse order"""
#to reverse the original order of a list(not alphabetically), you can use the reverse() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

"""Finding the length of a list"""
#quickly find the length of a list by using the len() funciton
#Python starts the count with one

cars = ['bmw', 'audi', 'toyota', 'subaru', 'honda', 'mazda', 'ford'] 
print(len(cars)) #7