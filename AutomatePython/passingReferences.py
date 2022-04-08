def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam) # eggs function will append 'Hello' into spam list
# [1, 2, 3, 'Hello']
