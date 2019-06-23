# Making a Game of IT - Day 2 - Pygame

Note: our introduction into pygame is taken/adapted from: [https://inventwithpython.com/pygame/](https://inventwithpython.com/pygame/)

<!-- TOC -->

- [Pygame - Graphics](#pygame---graphics)
- [Pygame - Animation](#pygame---animation)
- [Pygame - Controls](#pygame---controls)
- [Pygame - Text](#pygame---text)
- [Pygame - Collisions](#pygame---collisions)
- [Putting it all together](#putting-it-all-together)

<!-- /TOC -->

## Pygame - Graphics

## Pygame - Animation

Moving on from drawing static images to simple animations isn't too difficult in pygame. We animate images by drawing an image to the screen, and then quickly drawing a slightly different image to the screen.

{% include codeinclude.html file='catimation.py' %}

## Pygame - Controls

## Pygame - Text

{% include codeinclude.html file='text.py' %}

## Pygame - Collisions

{% include codeinclude.html file='collision.py' %}

## Putting it all together

In this example, we're going to have pygame shoot projectiles from the mouse when the mouse is clicked:

{% include codeinclude.html file='bullets.py' %}

Can we adjust the program to have a character rectangle that the player moves around with arrow keys, and when the player presses the spacebar, it fires projectiles (instead of the mouse)?

<!-- {% include codeinclude.html file='bullets_game_v0.py' %} -->

If you did that, can you use WASD to change the direction that the projectiles are shot from the character's rectangle? (e.g., 'w' points projectiles upward, 'd' to the right, etc)

<!-- {% include codeinclude.html file='bullets_game_v1.py' %} -->