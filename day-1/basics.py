'''
Goals:
- Comments
- Printing things to the 'screen' (console)
- Variables
    - Converting between different types of variables
    - Maths!
- Getting user input
'''

####################################
#        Comments in Python
####################################

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

# Why use comments?
# - (1) For future you!
# - (2) For anyone else who might read your code!

#####################################
#  Printing to the screen
#####################################
# We can use the 'print' instruction to print things to the screen
print("Hello world")
print("My name is Alex Lalejini, and I am 26 years old.")
print("I thought Avengers: Endgame was just okay.")

# Note that every time you run your program, those sentences are always printed
# in the same order. Python programs are executed procecurally, instruction-by-instruction,
# from top to bottom.

#####################################
#       What is a variable?
#####################################
# We use variables to store and later refer to data or values.
# I.e., they give us a place to put stuff and let us refer to that stuff later.

# For example, we can assign a 'string' to a variable:
first_name = "Alex"     # This is a string
last_name = "Lalejini"  # This is also a string

# We could also assign numbers to a variable:
age = 26                # This is an integer
half_of_three = 3.5     # This is a float (i.e., it has a decimal)

# We can print out the values of previously assigned variables.
print(first_name)
print(last_name)

# We can 'add' strings together
print(first_name + last_name)
# It's sort of ugly without a space
print(first_name + " " + last_name)

full_name = first_name + " " + last_name
print(full_name)

# Will fail:
# print("My name is " + full_name + ", and I am " + age + " years old.")

# Python can't 'add' together a string variable and a number variable
print("My name is " + full_name + ", and I am " + str(age) + " years old.")

# We can use the str() instruction to convert things into strings
# We can use the int() instruction to convert things into integers
# We can use the float() instruction to convert things into floats

# Python can be used as a really fancy calculator:
twice_my_age = 2 * age   # multiplication
in_ten_years = 10 + age  # addition
half_my_age = age / 2    # division

# If you want to use python to help you with future math homework assignments, this
# might be of use: https://docs.python.org/3/library/math.html

#####################################
#    Getting input from the user
#####################################
# We can use the input() instruction to request information from the user

user_input = input("I demand your input: ")
print("So that I can spit it right back at you: " + user_input)

# CHALLENGE: Adjust your program so that it takes a user's name and age
#            in as input, and prints the year they were born.


#####################################
# Extra challenges
#####################################

"""
- What happens when you expect numeric input from the user but they give you a string (e.g. 'hello world')?
  - CONCEPT: try/catch statements
- What are some special characters that aren't obvious in how we can include them
    in a python string? (e.g., newlines, tabs) How can we represent these in a Python
    string?
"""