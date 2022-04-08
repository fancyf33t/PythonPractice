 # Write your code here :-)
import random, sys #random will import random functionality; sys to help close program

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, lossess, and ties
wins = 0
losses = 0
ties = 0

while True: # The main game loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # Player input loop
        print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit')
        player_move = input()
        if player_move == 'q':
            sys.exit() # Quit the program; not the same as break?
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break # Break out of he player input loop
        print('Type one of r, p, s, or q.')
    #Display what the player chose:
    if player_move == 'r':
        print('ROCK vesus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    #Display what the computer chose:
    random_number = random.randint(1,3)
    if random_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif random_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif random_number == 3:
        computer_move = 's'
        print('SCISSORS')

    #Display and record the win/loss/tie:
    if player_move == computer_move:
        print("It's a tie!")
        ties = ties + 1
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        losses = losses + 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose!')
        losses = losses + 1
