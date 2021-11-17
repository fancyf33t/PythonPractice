dimensions = (200, 50, 1000)
print(dimensions[0])
print(dimensions[1])
print(dimensions[2])

# dimensions = (200, 50, 1000)
# dimensions[2] = 500 #tuples are immutable and cannot be changed

for dimension in dimensions:
    print(dimension)
    print(f"{dimension} is one dimension provided.")
#just stay calm and keep working...

dimensions = (200, 50, 1000)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (300, 90, 1)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
#tuples can't be changed but written over? that is slightly confusing...
#"Although you can't modify a tuple, you can assign a new value to a variable that represents a tuple. (p67)"
