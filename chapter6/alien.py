alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points.")

print('*************************************')

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print('****************************')

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

print('****************************************')

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow' #to modify a value in a dictionary, give the name of the dictionary with the key in square brackets and then the new value you want associated with that key
print(f"The alien is now {alien_0['color']}.")

print('*******************************')

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'} #key:value separated by colons
#alien_0 is a ditionary that has a stored x_position, stored y_position, and a stored speed. The if statement will run through the dictionary in search of a passing condition.
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow': #this is an if statement testing for a passing condition.
    x_increment = 1
elif alien_0['speed'] == 'medium': #this is an elif statement testing for a passing condition
    x_increment = 2
else:
    #this will be the fast alien (which will run as a default result)
    x_increment = 3

#the new position is the old position plus the increment
#"you need to get a better understanding of this process before moving on."
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}.")
#since the previously stored x_position was 0, the 'medium' speed that was tested will add 2 to the x_position of alien_0

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
#in order to completely remove a key:value pair, use the del statement while calling on the key

del alien_0['points']
print(alien_0)
#'points' has been removed permanently and must be added back manually?

alien_0 = {'points': 10}
print(alien_0)