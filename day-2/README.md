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

### Hello, Rectangle

First, let's import the pygame package and initialize its modules.

```python3
import pygame

pygame.init()
```

Let's set up game screen.

```python3
screen = pygame.display.set_mode([1200, 800])
pygame.display.set_caption("Alien Invasion")
```

Let's define some colors using RGB codes (red, green, blue).
Each color is a three-item list where the intensity of each hue is described from 0 (low intensity) to 255 (high intensity).


```python3
RED = [255, 0, 0]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
```

**Comprehension Question**
What would the code for `GREEN` be?
For `BLUE`?

In the coordinate system you know from math class, the origin is on the bottom left.
```
  ^
5 |
4 |
3 |      (3,2)
2 |     *
1 |
0 +------------->
  0 1 2 3 4 5
```

The coordinates in pygame are a little different: the origin is on the top left.

```
   0 1 2 3 4 5
0 +------------->
1 |
2 |      *
3 |       (3,2)
4 |
5 |
  |
```

The x-axis works exactly like you're used to, but now larger y values mean closer to the bottom of the screen.

We've got color and coordinates figured out, so we're ready to draw our rectangle.
First, we define the rectangle shape.
The arguments, in order, represent `left`, `top`, `width`, and `height`.
The arguments `left` and `top` say where the

```python3
first_rect = pygame.Rect(
    100, # left
    200, # top
    30,  # width
    150  # height
  )

pygame.draw.rect(screen, RED, first_rect)

pygame.display.flip() # refresh the screen
```

Note that we have to call `pygame.display.flip()` to get pygame to draw our changes to the screen.
This is so we can make a whole mess of changes one-by-one and then render them all at once efficiently.


**Challenge:**
Can you draw
* a red rectangle in the top left quarter of the screen,
* a blue rectangle on the top right quarter of the screen,
* a green rectangle on the bottom half of the screen?

### Getting in Shape

We can use pygame to draw a line connecting a start point to an end point.

```python3
pygame.draw.line(
    screen,     # where to draw the line
    WHITE,      # line color
    [0, 0],     # x,y start point
    [100, 100], # x,y end point
    5           # line width
  )
```

To draw a circle or an ellipse (a squished circle), we specify a bounding rectangle.
Then, we draw the ellipse inside that rectangle.

```python3
ellipse_rect = pygame.Rect(
    400, # left
    400, # top
    40,  # width
    80   # height
  )
pygame.draw.ellipse(
  screen,       # where to draw ellipse
  RED,          # color
  ellipse_rect  # rectangle to draw inside
)
pygame.display.flip() # refresh the screen
```

Mathematically, a polygon is defined by series of straight paths between vertices.
For example, triangles, squares, and pentagons are all polygons.

In pygame, we define a polygon just like in math: using a list of `(x,y)` vertex coordinates.

```python3
pygame.draw.polygon(
    screen,                     # where to draw the polygon
    RED,                        # color
    [[0,0], [200,200], [100,0]] # x,y coordinates of vertices
  )
pygame.display.flip() # refresh the screen
```

**Challenge:**
Can you draw a simple house using pygame shapes?

### The Cat's Meow

We've got cat scratch fever and want to render a cat in PyGame.
We could try to use shapes, but drawing even just a recognizable cat would be a lot of work --- lots of ellipses and lines!
A better idea is just to draw an image of a cat.

To make this next code work, you need to have the image [cat.png](/media/cat.png) saved into the same folder as your Python file.

First, we have to load the image from file.
(Note: in a game, we usually only want to do this once.)
Then, we ask for the pygame rectangle the same size as our image and recenter it to the `x,y` coordinates where we'd like it to go.
Finally, we `blit` the image into the rectangle we set up and refresh the screen.

```python3
cat_image = pygame.image.load('cat.png')
cat_rect = cat_image.get_rect()
cat_rect.center = [100, 400]

screen.blit(cat_image, cat_rect)

pygame.display.flip() # refresh the screen
```

**Challenge:**
1. Can you draw the cat in your house's window?
2. Download another image from the interwebs and add it to your house.

## Pygame - Animation

Moving on from drawing static images to simple animations isn't too difficult in pygame. We animate images by drawing an image to the screen, and then quickly drawing a slightly different image to the screen.

{% include codeinclude.html file='catimation.py' %}

## Pygame - Controls

So far, we've only used `input` to ask for user input as text.
Now, we'll use pygame to handle real-time keyboard and mouse input!

### Keyed Up

```python3
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        print("User asked to quit.")
    elif event.type == pygame.KEYDOWN:
        print("User pressed a key.")
    elif event.type == pygame.KEYUP:
        print("User let go of a key.")
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print("User pressed a mouse button")
```

### Mousing Around

```python3
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.KEYDOWN:
        # Keydown event!
        if event.key == pygame.K_SPACE:
            # Fire a bullet
            print("pressed space")
            pos = [0, 0]
            if character["dir"] == "up":
                pos = character["rect"].midtop
                h = bullet_width
                w = bullet_height
            elif character["dir"] == "down":
                pos = character["rect"].midbottom
                h = bullet_width
                w = bullet_height
            elif character["dir"] == "right":
                pos = character["rect"].midright
                h = bullet_height
                w = bullet_width
            elif character["dir"] == "left":
                pos = character["rect"].midleft
                h = bullet_height
                w = bullet_width
            bullet = {"rect": pygame.Rect(pos[0], pos[1], w, h), "dir": character["dir"]}
            bullets.append(bullet)
        if event.key == pygame.K_w:
            character["dir"] = "up"
        if event.key == pygame.K_d:
            character["dir"] = "right"
        if event.key == pygame.K_s:
            character["dir"] = "down"
        if event.key == pygame.K_a:
            character["dir"] = "left"
```

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