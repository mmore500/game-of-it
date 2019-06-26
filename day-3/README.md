# Making a Game of IT - Day 3 - Pygame

<!-- TOC -->

- [Logistics and announcements](#logistics-and-announcements)
- [Pygame - Sprites and More Collision(?)](#pygame---sprites-and-more-collision)
- [Pygame - Buttons and Menus](#pygame---buttons-and-menus)
- [LUNCH SPECIAL TASK](#lunch-special-task)
- [Pygame - Music and sound effects](#pygame---music-and-sound-effects)
- [Pygame - High-level structure](#pygame---high-level-structure)

<!-- /TOC -->

## Logistics and announcements

- @Lunch today: brainstorm ideas for the type of game you'd like to make!
  - This afternoon, we'll have everyone turn in their preferences, and we'll use that information to make teams.
- Posting some of your programs
  - There were lots of super neat pygame programs yesterday (e.g., 1000s of cats moving around the screen); if you'd like us to post (on this website) any of your (working) pygame programs, let us know! For any programs you want posted, we'll want a short description of what it does to go along with it.

## Pygame - Sprites and More Collision(?)

## Pygame - Buttons and Menus

Buttons in pygame are very simple: they're rectangles that we draw on the screen, and we detect button presses by detecting collisions between the mouse pointer and the button rectangle when the player clicks.
We can also use an image as a button.
You'll need to download [red-button.png](/media/red-button.png) into the folder containing your Python file for the code below to work.

{% include codeinclude.html file='buttons.py' %}

Menus are just several buttons strung together.
We can make a menu screen by having multiple game modes.
In the example below, we have two game modes:
1. a title screen mode and
2. a menu screen mode.
In the menu screen, the player uses the arrow keys to navigate (we could have used the mouse here instead), and presses enter to make a selection.

{% include codeinclude.html file='menu.py' %}

## LUNCH SPECIAL TASK

Brainstorm the _type_ of game you're interested in making.

For example...

## Pygame - Music and sound effects

## Pygame - High-level structure

<!-- {% include codeinclude.html file='block_catchy.py' %} -->
