'''
Game of Hangman
By: Josh

Skills:
- Looping
- Lists
'''

secret = 'banana'
guesses = []

rnd = 1
has_won = False

while rnd <= 10:
    print('Round', rnd)

    # Get a guess from the player (we only one one letter)
    guess = input('Guess a letter: ')
    print('You guessed:', guess)

    # We have some requirements for player input: e.g., len
    if len(guess) != 1:
        print('Only one letter at a time, please')
        continue

    if not guess.islower():
        print('Must be a lowercase letter.')
        continue

    guesses.append(guess)

    # Reveal the known/unknown letters
    revealed = ''
    for letter in secret:
        if letter in guesses:
            revealed += letter
        else:
            revealed += '*'

    print('Revealed so far: ', revealed)

    # How do we know if the player won?
    is_all_revealed =  '*' not in revealed

    if is_all_revealed:
        has_won = True
        print('You won!')
        break

    rnd += 1

if not has_won:
    print('YOU FAILURE!')