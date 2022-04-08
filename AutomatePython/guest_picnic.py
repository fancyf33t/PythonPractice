allGuests = { # these are nested dictionaries to help store information
    'Alice': {'apples': 5, 'pretzels': 12},
    'Bob': {'ham sandwiches': 3, 'apples': 2},
    'Carol': {'cups': 3, 'apple pies': 1}
}
# print(allGuests)
def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought
print('Number of things being brought:')
print('+=============================+')
print('- Apples  ' + str(totalBrought(allGuests, 'apples'))) # using the str() to stringify possible dictionary values
print('- Cups  ' + str(totalBrought(allGuests, 'cups')))
print('- Ham Sandwiches  ' + str(totalBrought(allGuests, 'ham sandwiches')))
print('- Cake  ' + str(totalBrought(allGuests, 'cake')))
