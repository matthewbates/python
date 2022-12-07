
#* LISTS
# a fundamental data structure for organizing data (similar to a JavaScript array)
    # a comma separates each value
tasks = ["Install Python", "Learn Python", "Take a break"]

# count the number of items in a list using len()
# unlike JavaScript, the len() function is chained on BEFORE the argument, not after
print(len(tasks))

# you can also convert a range to a list
r = range(1, 10) #range(1, 10)
list(r) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

#* ACCESSING DATA IN LISTS
# lists ALWAYS start counting at zero index
friends = ["Jordan", "Aaron", "Ryan"]
print(friends[0]) #Jordan
print(friends[1]) #Aaron
print(friends[2]) #Ryan

# you can use a negative number to index backwards
print(friends[-1]) #Ryan

#* ITERATING OVER LISTS
# using a for loop
colors = ["purple", "teal", "magenta"]
for color in colors:
    print(color) #color, teal, magenta

# using a while loop
numbers = [1, 2, 3, 4]
i = 0
while i < len(numbers):
    print(f"{i}: {colors[i]}")
    # don't forget to increment i or else it will become an infinite loop!
    i += 1 #1, 2, 3, 4
