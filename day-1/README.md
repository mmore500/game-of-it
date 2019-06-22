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
  - [Challenges](#challenges)
- [Python - conditionals and loops](#python---conditionals-and-loops)
- [Python - data structures](#python---data-structures)

<!-- /TOC -->

## Introductions & Getting Started

Why python?


### Getting Started

- Make your own directory on the shared network drive.
- [Thonny](https://thonny.org/) _should_ already be installed on your computer!
  - Thonny is an Integrated Development Environment (IDE) for Python. In simpler terms, it's the application you'll use to edit and run your Python programs.
  - There should be a shortcut on your desktop for Thonny. If you can't find it (or it doesn't work), let us know!

## Python - the very basics

The code for this section is in [basics.py](./basics.py).

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

### Challenges

- (1) Write a program that take a user's name and age in as input, and prints the year they were born.
- (2) Adjust program so that user's name is printed in ALL CAPS (hint: checkout Python's string documentation)
- (3) What are some special characters that aren't obvious in how we can include them in a python string (e.g., so we can print them)? Think about things you use all the time when writing an essay or an email. E.g., what might you start a paragraph with?

<!-- ### Example code -->

<!-- {% include linkinclude.html file='basics.py' %} -->

## Python - conditionals and loops

Conditional statements (syntax: `if`) allow your code to make decisions based on input.
Code inside an `if` block is only executed if the test next to the `if` evaluates to `True`.

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

Sometimes, we want to run a code block once for each element in a collection.
We could print `"Bloody Mary!"` once for each number 0 through 12.

```python
for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
  print("Bloody Mary!", i)
```

Python gives us a nice way to count with a for loop.
The `range(n)` function makes a collection of integers from 0 through `(n-1)`.
(This way, when code inside `for i in range(n):` runs `n` times.)

```python
for i in range(13):
  print("Bloody Mary!", i)
```



{% include codeinclude.html file='simon_says.py' %}

{% include codeinclude.html file='rock_paper_scissors.py' %}

## Python - data structures
