# Making a Game of IT - Day 1

<!-- TOC -->

- [Introductions & Getting Started](#introductions--getting-started)
  - [Getting Started](#getting-started)
- [Python - the very basics](#python---the-very-basics)
  - [Comments in Python](#comments-in-python)
  - [Printing to the screen](#printing-to-the-screen)
  - [What is a variable?](#what-is-a-variable)
- [Python - conditionals and loops](#python---conditionals-and-loops)
- [Python - data structures](#python---data-structures)

<!-- /TOC -->

## Introductions & Getting Started

Why python?


### Getting Started

- Make your own directory on the shared network drive.
- Thonny
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
print("I thought Avengers: Endgame was just okay.")
```

Note that every time you run your program, those sentences are in the same order.
Python programs are executed _procedurally_, instruction-by-instruction, from
top to bottom.

### What is a variable?

We use variables to store and later refer to data or values. In other words,
we can _assign_ values to variables, and then we can use those variables to later
refer to their values.

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




## Python - conditionals and loops

## Python - data structures
