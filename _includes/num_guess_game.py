'''
guessing.py

Guessing game! Guess a number between (inclusive) 1 and 100.

Skills
- variables/user input
- looping
- generating random numbers
'''

import random

secret = random.randint(1, 101) # Question: why 101 instead of 100?
print('Secret is', secret) # sanity check our secret generator

while True:
    guess = int(input('Guess my secret: '))

    # (1) if user guessed correctly, they win!
    if guess == secret:
        print('YOU WON!! SUCH VICTORY!')
        break

    # (2) Can we give the player some hints?
    # - What sorts of hints might we want to give a player?
    if guess < 1 or guess > 100:
        print('Hint: 1-100')

    if guess > secret:
        print('Too high')
    else:
        print('Too low')

print('End')

# Challenge: Get rid of the magic numbers (min secret value and max secret value)
# Challenge: Tell the user how many guesses it took them to win
# Challenge question: What's the optimal strategy for playing this game?
# SUPER CHALLENGE: Make input request safe from bad user input
# - e.g., with try/catch or isnumeric