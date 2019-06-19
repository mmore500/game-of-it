'''
data_structures.py

We can compose multiple simple types of values into more complicated structures...
like lists!
'''

# We can assign a list to a variable:
pet_names = ['Yogi', 'Boomer', 'Gunther', 'Banana']

# It's easy to loop over a list
for name in pet_names:
    print(name)

# Each item in a list is at a particular position.
# NOTE: Positions in a list start at '0'
print(pet_names[0])
print(pet_names[1])
# We can get the last value in the list by:
print(pet_names[-1])

# We can modify the value of something in the list
pet_names[1] = "BOOMER"
print(pet_names[1])

# Challenge/question: How might we get second-to-last value in the list?
# Question: What happens if we try to get the name at position 5?

# It's often useful to check to see if a particular value is in the list
print("'Alex' in the list? " + str('Alex' in pet_names))
print("'Yogi' in the list? " + str('Yogi' in pet_names))
print("'BANANA' in the list? " + str('BANANA' in pet_names))    # ???
print("'gunther' in the list? " + str('gunther' in pet_names))   # ???

# We can append things to the end of the list:
pet_names.append("Doggo")
# We can print the entire list
print(pet_names)
# We can insert things into the list
pet_names.insert(1, "Fishy")
print(pet_names)
# We can remove things (by value)
pet_names.remove("Gunther")
print(pet_names)
# We can remove things by position
pet_names.pop(1)

# Wait, how long is our list now?
print(len(pet_names))

# Things in a list have an order to them
sorted_pet_names = sorted(pet_names)
print(sorted_pet_names)

reverse_sorted_pet_names = sorted(pet_names, reverse=True)
print(reverse_sorted_pet_names)

# We can also remove everything in the list
pet_names.clear()
print(pet_names)

# Challenges
# - Make a list of 10 numbers (of your choosing):
#   - calculate the average
#   - get the difference between the max and the minimum value
# - Dictionaries - key:value pairs
#   - More info here: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# - HARDMODE: list comprehensions - create a list (1,2,3,...,1000) using a list comprehension

# More things you can do with lists: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists