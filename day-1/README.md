# Making a Game of IT - Day 1

<!-- TOC -->

- [Introductions & Getting Started](#introductions--getting-started)
  - [Getting Started](#getting-started)
- [Python - the very basics](#python---the-very-basics)
  - [Comments in Python](#comments-in-python)
  - [Printing to the screen](#printing-to-the-screen)
  - [What is a variable?](#what-is-a-variable)
  - [Python can be used as a glorified calculator](#python-can-be-used-as-a-glorified-calculator)
  - [Getting user input](#getting-user-input)
  - [Working with strings](#working-with-strings)
  - [Basics - Challenges](#basics---challenges)
  - [Basics - Example code](#basics---example-code)
- [Python - conditionals and loops](#python---conditionals-and-loops)
- [Python - data structures](#python---data-structures)
  - [Lists](#lists)
  - [Dictionaries](#dictionaries)
  - [Data structures - example games](#data-structures---example-games)
    - [World guessing game](#world-guessing-game)
    - [Simon Says](#simon-says)

<!-- /TOC -->

## Introductions & Getting Started

Why python?


### Getting Started

- Make your own directory on the shared network drive.
- [Thonny](https://thonny.org/) _should_ already be installed on your computer!
  - Thonny is an Integrated Development Environment (IDE) for Python. In simpler terms, it's the application you'll use to edit and run your Python programs.
  - There should be a shortcut on your desktop for Thonny. If you can't find it (or it doesn't work), let us know!

## Python - the very basics

The code for this section is in [basics.py](._includes/basics.py).

### Comments in Python

Comments give programmers a way to annotate their code.

```python
# '#' denotes a single-line comment. For example,
# This is a single-line comment!

"""
Three double quotes can be used to denote the start and end of a... you guessed it...
a multi-line comment!



This is all part of this multi-line comment!

And this, too!
"""

''' You can also use single quotes to denote a multi-line comment.

Remember, though, a multi-line comment started with three single-quotes must be
ended with three single-quotes!

For example, """
does not end this multi-line comment. But, '''

```

Why use comments?

- To document your programs!
  - (1) For future you to understand what past you was thinking
  - (2) For other programmers who might read or use your code

### Printing to the screen

We can use the `print` instruction to print things to the screen:

```python
print("Hello world")
print("My name is Alex Lalejini")
print("I'm 26 years old.")
print("Ikea is adult disney land.")
```

Note that every time you run your program, those sentences are in the same order.
Python programs are executed _procedurally_, instruction-by-instruction, from
top to bottom.

### What is a variable?

We use variables to store data and subsequently refer to that data. As a pet name lets us to refer to our 🐶, variables give us a way to refer to our data.

Variables in python must _begin_ with a letter or underscore, but after the first character letters, numbers, and underscores are 👌. In contrast to pet names (where your pet does not care about the capitalization of their name), python variables are case sensitive (i.e, 'DOGGO' is not the same as 'doggo').

We can assign _'strings'_ to variables:

```python
first_name = "Alex"     # This is a string
last_name = "Lalejini"  # This is also a string
```

In this above example, `first_name` is a variable. I assigned it the value `"Alex"`
using the assignment operator `=`.

We can also assign _numbers_ to variables:

```python
age = 26              # This is an integer
half_of_three = 3.5   # This is a float (i.e., it has a decimal)
```

We can _refer_ to previously assigned variables. For example, we can print out
the values of some of our variables:

```python
print(first_name)
print(last_name)
print(age)
```

### Python can be used as a glorified calculator

You can (and we will) use python as a fancy calculator. All the classics are available out of the box: addition `+`, subtraction `-`, multiplication `*`, division `/`, modulus `%` (remainder), and exponentiation `**`.

In python:
```python
this_year = 2019
my_age = 26

twice_my_age = 2 * age

ten_years_from_now = this_year + 10

year_born = this_year - my_age

half_my_age = age / 2
```

Just like in math class, you can enforce a particular order of operations using parentheses:

```python
a = (1 + 1) * (2 + 2) # = 8
# is different from
b = 1 + 1 * 2 + 2     # = 5
```



More math is available in Python's [math module](https://docs.python.org/3/library/math.html).

### Getting user input

We can use python's `input()` instruction to request information from the user:

```python
user_input = input("I demand input: ")
```

In the code above, whatever the user types in gets stored in `user_input`. The string `"I demand input: "` is used as the prompt for input.

### Working with strings

Find more things you can do to strings here: [https://docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

### Basics - Challenges

- (1) Write a program that take a user's name and age in as input, and prints the year they were born.
- (2) Adjust program so that user's name is printed in ALL CAPS (hint: checkout Python's string documentation)
- (3) What are some special characters that aren't obvious in how we can include them in a python string (e.g., so we can print them)? Think about things you use all the time when writing an essay or an email. E.g., what might you start a paragraph with?

### Basics - Example code

{% include linkinclude.html file='basics.py' %}

## Python - conditionals and loops

### Boolean Operators

The operator `==` will tell you if two things are equal.
Note that one equal sign `=` means "assignment" and two equals signs `==` means "test equal."
If `x` and `y` are equal, `x == y` will turn into `True`.
If `x` and `y` are not equal, `x == y` will turn into `False`.

For example,
```
print(11 == 11)
print("hello" == "hello")
```

`<` will tell you if the left thing is smaller than the right thing.

`>` will tell you if the left thing is bigger than the right thing.

`<=` and `>=` will do exactly what you expect.

**Challenge:**
Which of the following three are equal to `1111`?
* `10 * 111`,
* `57 * 33`, or
* `11 * 101`

Which is bigger, `123 * 45` or `8765`?

Can test whether a user said "yes" using `input`?

### `if`, `elif`, and `else`

Conditional statements (syntax: `if`) allow your code to make decisions based on input.
Code inside an `if` block is only executed if the test next to the `if` evaluates to `True`.
*Note how whitespace at the beginning of a line determines which block a line of code is in.*

```python
print("duu du duu du dududu...")
print("duu du duu du dududu...")
if input("Is there something strange in your neighborhood? ") == "yes":
  print("who ya gonna call??? ghostbusters!!")
```

The syntax `elif` (else if) allows you to perform a subsequent test if the first `if` doesn't evaluate to `True`.
The syntax `else` is a catch-all that executes at the end of a series of `if` and `elif` tests if nothing else has triggered.

```python
print("duu du duu du dududu...")
print("duu du duu du dududu...")
if input("Is there something strange in your neighborhood? ") == "yes":
  print("who ya gonna call??? ghostbusters!!")
elif input("An invisible man... sleepin in your bed? ") == "yes":
  print("who ya gonna call??? ghostbusters!!")
elif input("Mm.. if you've had a dose... of a  freaky ghost baby? ") == "yes":
  print("who ya gonna call??? ghostbusters!!")
else:
  print("you better NOT call... ghostbusters!")
```

**Challenge:**
Ghostbusters is a PG-13 movie.
Ask the user for their age and then tell them if they're ready to see Ghostbusters.
If they're younger than thirteen, tell them no!
Else, if they're older than 113, tell them that they're the oldest person in the world.
Otherwise, tell them they're cleared to watch Ghostbusters.

### `while` and `break`

According to urban legend, saying "bloody mary" 13x into a mirror will summon a scary ghost.
Here's one way of doing that.

```python
print("Bloody Mary!")
print("Bloody Mary!")
print("Bloody Mary!")
print("Bloody Mary!")
print("Bloody Mary!")
print("Bloody Mary!")
print("Bloody Mary!")
print("Bloody Mary!")
print("Bloody Mary!")
print("Bloody Mary!")
print("Bloody Mary!")
print("Bloody Mary!")
print("Bloody Mary!")
```

Pretty annoying, right?
The syntax `while` repeats a block of code until the test next to it evaluates `False`.

```python
while input("Keep going?") == "yes":
  print("Bloody Mary!")
```

We can make Python count to 13 for us.
The variable `i` increases by one until it reaches 13.

```python
i = 0
while i < 13:
  print("Bloody Mary!", i)
  i = i + 1
```

What if we want a way to back out of summoning the scary mirror ghost?
Python's `break` statement allows the programmer to end a loop.
Let's put a `break` statement inside an `if` to stop the summoning if we get scared.

```python
i = 0
while i < 13:
  print("Bloody Mary!", i)
  i = i + 1
  if input("Scared yet??? ") == "yes":
    print("ok let's stop")
    break
```

### `for` and `range`

Programmers want to execute a code block `n` times so often that Python gives us a way to do just that: a `for` loop coupled with the function `range(0,n)`.
Like so,

```python
for i in range(0,13):
  print("Bloody Mary!", i)
```

Conceptually, `for` iterates over each element `in` a collection --- it puts each element in the collection one at a time into the variable `i`.
The function `range(0,n-1)` creates a collection with the numbers `0` through `n-1`.
(This way, when code inside `for i in range(n):` runs `n` times.)
If we wanted the numbers 1 through 13 instead of 0 through twelve, we would write `range(1,13)`. 


**Comprehension Question:**
How many times will "Boo!" get printed?

```python
for i in range(3):
  for j in range(3):
    print("Boo!")
```

**Challenge:**
There's one ghost in the first room.
There's two ghosts in the second room.
There's three ghosts in the third room... and so on and so forth.
There's thirteen rooms in this haunted 80's penthouse.
Can you use math and a loop to calculate how many ghosts we're going to run into total?

### Number Guessing Game

Let's put it all together to make a number guessing game.
Python will randomly choose a number and then we'll make successive guesses until we get it.
Each time we guess, Python will tell us if our guess was too low or too high.

{% include codeinclude.html file='num_guess_game.py' %}

**Extra Challenge:**
Can you write a program that lets two players play Rock, Paper, Scissors against eachother?
Your program should request player 1 and player 2's choices (rock, paper, or scissors), and determine whether player 1 wins, player 2 wins, or the two players tied.

## Python - data structures

### Lists

We can compose simple data types (e.g., strings, integers, etc) into more complex data structures.

A list, for example, lets us store a sequence of values (often referred to as elements):

```python
pet_names = ['Yogi', 'Boomer', 'Gunther', 'Banana']
```

You can access and reassign individual positions (or indexes) in a list using square brackets `[]`. NOTE: lists in python always start at 0 (e.g., 'Yogi' in our example is at position 0 of the `pet_names` list).

```python
print(pet_names[0]) # will print Yogi
print(pet_names[1]) # will print Boomer
print(pet_names[3]) # will print Banana

# We can access a list with negative numbers, too...
print(pet_names[-1]) # will print Banana
```

**CHALLENGE QUESTION**: how might we get the second-to-last value in the list?

We can modify the value of something in the list:

```python
pet_names[1] = "BOOMER"
print(pet_names[1]) # will print BOOMER
```

A word of warning: if you try to index into a position beyond the size of the list, python will yell at you: `IndexError: list index out of range`.

```python
pet_names[4] # will give you an error
pet_names[100] # will give you an error
pet_names[-4] # will give you an error
```

We can loop over a list using a for loop:

```python
for name in pet_names:
    print(name)
```

It's often useful to check to see if a particular value is in the list:

```python
print("'Alex' in the list? " + str('Alex' in pet_names))         # no
print("'Yogi' in the list? " + str('Yogi' in pet_names))         # yes
print("'BANANA' in the list? " + str('BANANA' in pet_names))     # nope - remember, python is case sensitive
print("'gunther' in the list? " + str('gunther' in pet_names))   # nope
```

We can append things to the end of lists:

```python
pet_names.append("Doggo")
# We can print the entire list
print(pet_names)
```

We can insert things into the list at a particular position:

```python
pet_names.insert(1, "Fishy")
print(pet_names)
```

We can remove a particular value from the list:

```python
pet_names.remove("Gunther")
print(pet_names)
```

We can remove something from the list by position:

```python
pet_names.pop(1)
print(pet_names)
```

Wait, how long is our list? We can use the `len()` instruction to check:

```python
list_len = len(pet_names)
print(list_len)
# We could also:
print(len(list_len))
```

We can sort a list:

```python
sorted_pet_names = sorted(pet_names)
print(sorted_pet_names)

# What if we want reverse order?
reverse_sorted_pet_names = sorted(pet_names, reverse=True)
print(reverse_sorted_pet_names)
```

We can remove everything from a list:
```python
pet_names.clear()
print(pet_names)
```

For more things you can do with lists see: [https://docs.python.org/3/tutorial/datastructures.html#more-on-lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

**CHALLENGES**

- Make a list of 10 numbers (of your choosing)
  - calculate the average
  - get the difference between the max and the minimum value

### Dictionaries

We won't spend much time on dictionaries for the moment, but we'll point them out because they're super useful.

A dictionary (often refered to as a `dict`) in Python is a set of key-value pairs.

In Python, dictionaries are denoted using `{}`.

```python
info_dict = {"name": "Dumbledore", "age": 115}
```

In the above example, we created a dictionary with 3 entries with the following keys: `"name"`, `"age"`.

We access the values in a dictionary using their keys:

```python
print(info_dict["name"])                  # Dumbledore
print(info_dict["age"])                   # 115
```

We can update the value associated with a particular key:

```python
info_dict["name"] = "Harry Potter"
print(info_dict["name"])            # Harry Potter
```

We can add entries to a dictionary:

```python
info_dict["muggle"] = False
print(info_dict)
```

**CHALLENGE**: Make a dictionary where at least one entry has a list for a value and another entry has a dictionary for a value.

For more on dictionaries: [ttps://docs.python.org/3/tutorial/datastructures.html#dictionaries](ttps://docs.python.org/3/tutorial/datastructures.html#dictionaries)

{% include linkinclude.html file='data_structures.py' %}

### Data structures - example games

#### World guessing game

In the word guessing game, the programmer has selected a secret word, and the player has 10 rounds to guess reveal what the secret is by guessing one letter at a time.

#### Simon Says

Game description:

Simon says is played in rounds. Starting the game with and empty list, the program selects a random letter each round. The program prints the chosen letter for the player to see. The player must then input each letter that the program previously output. Any deviation from the correct sequence results in a loss. The player's goal is to achieve as high a score as possible.


Example gameplay:

```
Simon says:  B
> B
Simon says: C
> B
> C
Simon says: A
> B
> C
> A
Simon says: C
> B
> C
> A
> C
Simon says: D
> C
WRONG! Final score = 4
```

In the above example, the program output all of the 'simon says' lines (using `print("Simon says:", letter)`), and player input (using `input(">")`) is given after the '>' prompt. When the player fails to repeat the full sequence, the player loses, and the game reports their final score.

After you have a working game please put up a green sticky
Then add the following optional features:

- Ensure that the user is only allowed to select a valid option (prompting them again if necessary)
- Change the elements that are being tested to (‘Rock’, ‘Paper’, or ‘Scissors’)
- For each input, let the player know how many more letters they need to provide for the round.
- Be sure to partition your code into functions with clear names and documentation
- If you have implemented all the above features, get up and help your neighbors who don’t have a green sticky.
