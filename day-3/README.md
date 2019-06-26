# Making a Game of IT - Day 3 - Pygame

<!-- TOC -->

- [Logistics and announcements](#logistics-and-announcements)
- [Pygame - Text, Buttons, and Menus](#pygame---text-buttons-and-menus)
  - [Text](#text)
  - [Buttons](#buttons)
  - [Menus](#menus)
- [LUNCH SPECIAL TASK](#lunch-special-task)
- [Pygame - Music and sound effects](#pygame---music-and-sound-effects)
- [Pygame - High-level structure](#pygame---high-level-structure)

<!-- /TOC -->

## Logistics and announcements

- @Lunch today: brainstorm ideas for the type of game you'd like to make!
  - This afternoon, we'll have everyone turn in their preferences, and we'll use that information to make teams.
- Posting some of your programs
  - There were lots of super neat pygame programs yesterday (e.g., 1000s of cats moving around the screen); if you'd like us to post (on this website) any of your (working) pygame programs, let us know! For any programs you want posted, we'll want a short description of what it does to go along with it.

## Pygame - Text, Buttons, and Menus

### Text

We skipped over rendering text yesterday, so let's revisit that...

Drawing text in pygame is _a lot_ like drawing images.

{% include codeinclude.html file='text_finished.py' %}

**CHALLENGE:** Make each of the three texts a different font type and font size.

### Buttons

Buttons in pygame are very simple: they're rectangles that we draw on the screen, and we detect button presses by detecting collisions between the mouse pointer and the button rectangle when the player clicks.
We can also use an image as a button.
You'll need to download [red-button.png](/media/red-button.png) into the folder containing your Python file for the code below to work.

{% include codeinclude.html file='buttons.py' %}

**CHALLENGE:** Add another button that resets the click counts for the other two buttons.
- Extra challenge: add a button that disables the other buttons (prevents them from being clicked)

### Menus

Menus are just several buttons strung together.
We can make a menu screen by having multiple game modes.
In the example below, we have two game modes:
1. a title screen mode and
2. a menu screen mode.
In the menu screen, the player uses the arrow keys to navigate (we could have used the mouse here instead), and presses enter to make a selection.

{% include codeinclude.html file='menu.py' %}

**CHALLENGE:** Add another option to the menu screen that changes the title screen's background

## LUNCH SPECIAL TASK

Brainstorm the _type_ of game you're interested in making.

For example...

## Pygame - Crank It Up to 11

In order for the following code to work, you'll need to download [beep1.ogg](/media/beep1.ogg), [Jeopardy.ogg](/media/Jeopardy.ogg), and [Tetris.ogg](/media/Tetris.ogg) into the folder containing your Python file.

### Sound Effects

First, let's talk about sound effects: recordings you want to play in response to an event on screen.
In the following example, we ring a bell in response to key presses.

```python3
import sys
import pygame

# Initialize and set up screen.
pygame.init()
screen = pygame.display.set_mode([100, 100])

clock = pygame.time.Clock()

beep_effect = pygame.mixer.Sound('beep1.ogg')

# main game loop
while True:

  # event-handling loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      print("bing!")
      beep_effect.play()

  clock.tick(60)

```

If you want to add your own sound effects, note that pygame has limited support for different formats: only WAV and OGG files work.

### Background Music

Next, let's cover background music --- something you'd want to be playing for the entire game or throughout a level of the game.
Unlike the sound effects, this sound is *streamed* instead of loaded all at once --- that means that pygame can handle big and long sound files efficiently here.
However, you can only have a single piece of background music playing at once.

If we want to just have one piece of background music playing the whole time, it would look like this.

```python3
import sys
import pygame

# Initialize and set up screen.
pygame.init()
screen = pygame.display.set_mode([100, 100])

clock = pygame.time.Clock()


pygame.mixer.music.load('Jeopardy.ogg')
pygame.mixer.music.play(-1) # how many loops to play? -1 means infinity

# main game loop
while True:

  # event-handling loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  clock.tick(60)
```

If we want to switch between two tracks (maybe on different levels, in different game modes, or between the title and game play screens) we use `itertools.cycle` to change out the currently playing track for an alternate on a keypress.

```python3
import sys
import pygame
import itertools

# Initialize and set up screen.
pygame.init()
screen = pygame.display.set_mode([100, 100])

clock = pygame.time.Clock()

filenames = itertools.cycle(['Tetris.ogg', 'Jeopardy.ogg'])

# main game loop
while True:

  # event-handling loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      print("switch tracks")
      pygame.mixer.music.stop()
      pygame.mixer.music.load(next(filenames))
      pygame.mixer.music.play(-1)

  clock.tick(60)
```

If you want to add your own background music, note that PyGame has limited support for different formats: only MP3 (some), OGG, XM, and MOD files work.

## Pygame - High-level structure

Let's take a crack at piecing together a complete pygame with a
1. start screen,
2. game play mode with scorekeeping and a lose condition, and
3. an end screen (with the option for replay).

{% include codeinclude.html file='block_catchy.py' %}
