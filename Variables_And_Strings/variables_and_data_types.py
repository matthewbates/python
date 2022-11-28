
#* VARIABLE ASSIGNMENT
# a variable in Python is like a variable in mathematics: it is a named symbol that holds a value
# variables are always assigned with the variable name on the left and the value on the right of the equals sign
# variables must be assigned before they are used

num_of_cats = "99"
print(num_of_cats)

#* DATA TYPES
# booleans (True (1) or False (0))
    # make sure these words are UPPERCASE
# integer (1, 2, 3, etc)
# string (a sequence of unicode characters, such as "Matthew")
# list (an ordered sequence of values of other data types [1, 2, 3] or ["a", "b", "c"])
    # think of a list like an array in JavaScript
# dictionary (a collection of key: values ("first_name": "Matthew", "last_name": "Bates"))

#* DYNAMIC TYPING
# you're allowed to reassign variables to different types
# variables can change types readily

#* THE SPECIAL VALUE NONE
# Pythons version of null

#* STRING ESCAPE CHARACTERS
# most used escape character is \n
print("hello\nthere")
print("He said, \"hello there!\"")
# print some mountains using escape
    # should output /\/\/\
print("/\\/\\/\\")

#* FORMATTING STRINGS
# there are several ways to format strings in Python to interpolate variables
    # the new way is called F-STRINGS
    # the string starts with an f
x = 10
formatted = f"I've told you {x} times already!"
print(formatted)
# FORMAT METHOD
x = 10
formatted = "I've told you {} times, already!".format(10)
print(formatted)

#* CONVERTING DATA TYPES
# in string interpolation, data types are implicity converted into string form
# you can also explicity convert variables by using the name of the built-in type as a function