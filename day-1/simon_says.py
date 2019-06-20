'''
Simple game of simon says

Skills:
- Lists, random, looping/conditionals
'''

import random

items = [] # Things simon said
while True:
    # What does simon say?
    new_item = random.choice('ABCDEF')
    items.append(new_item)
    print('Simon says: ', new_item)

    # Can the player correct repeat everything simon has said so far?
    was_wrong = False
    for correct_item in items:
        player_item = input('> ')
        if correct_item != player_item:
            was_wrong = True
            break

    if was_wrong:
        print('You lose')
        break