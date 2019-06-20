'''
Implements a one or two player game of rock-paper-scissors
'''

# Two-player version
print('Starting a game of ROCK-PAPER-SCISSORS')

# Get player 1's move
play = input('Player 1 move: ')
while play not in 'RPS' or len(play) != 1:
    print('Bad move')
    play = input('Player 1 move: ')

player_1_move = play

# Get player 2's move
play = input('Player 2 move: ')
while play not in 'RPS' or len(play) != 1:
    print('Bad move')
    play = input('Player 2 move: ')

player_2_move = play

# Determine a winner

# First, what are all of the possibilities?
# - What is the outcome of each?

# Question: How can we simplify (make it shorter) this code?
# - Tie:
# if player_1_move == player_2_move:
#     print('Tie game')

if player_1_move == 'R' and player_2_move == 'R':
    print('Tie game')

if player_1_move == 'R' and player_2_move == 'P':
    print('Paper covers rock!')
    print('Player 2 wins')

if player_1_move == 'R' and player_2_move == 'S':
    print('Rock smashes scissors!')
    print('Player 1 wins')

if player_1_move == 'P' and player_2_move == 'R':
    print('Paper covers rock!')
    print('Player 1 wins')

if player_1_move == 'P' and player_2_move == 'P':
    print('Tie game')

if player_1_move == 'P' and player_2_move == 'S':
    print('Scissors shred paper!')
    print('Player 2 wins')

if player_1_move == 'S' and player_2_move == 'R':
    print('Rock smashes scissors!')
    print('Player 2 wins')

if player_1_move == 'S' and player_2_move == 'P':
    print('Scissors shred paper!')
    print('Player 1 wins')

if player_1_move == 'S' and player_2_move == 'S':
    print('Tie game')

# Challenge: first to win three rounds
# Challenge: add ai player
# - static, random, copy-cat, opposite