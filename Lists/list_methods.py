
#* LIST METHODS: APPEND, INSERT, EXPAND
# APPEND
    # adds AN item to the end of a list
    # exactly the same as the .push() method in JavaScript
first_list = [1, 2, 3, 4]
first_list.append(5)
print(first_list) #1, 2, 3, 4, 5

# EXTEND
    # add to the end of a list all values passed to extend
    # this would be equivalent to the SPREAD OPERATOR in JavaScript
correct_list = [1, 2, 3, 4, 5]
correct_list.extend([5, 6, 7, 8])

# INSERT
    # insert an item at a given position
insert_list = [1, 2, 3, 4]
first_list.insert(2, "Hi!")
print(first_list) #1, 2, Hi!, 3, 4
first_list.insert(-1, "The end!")
print(first_list) #1, 2, Hi!, 3, The end!, 4
# alternatively you could do:
first_list.insert(len(first_list), "The end!")

# CLEAR
    # removes ALL items from the list
first_list = [1, 2, 3, 4]
first_list.clear()
print(first_list) #[]

# POP
    # removes the item at a given position from the list and returns it
    # if no index is specified, removes and returns LAST item from the list
    # EXACTLY the same as .pop() in JavaScript
first_list = [1, 2, 3, 4]
first_list.pop() #4
first_list.pop(1) #2

# REMOVE
    # remove the first item from the list whose value is x
    # throws a value error if the item is not found
    # EXACTLY the same as .shift() in JavaScript (.unshift() would ADD to the beginning of the array)
first_list = [1, 2, 3, 4]
first_list.remove(2)
print(first_list) #[1, 3, 4]

# INDEX
    # returns the index of the specified item in the list
    # same thing as .indexOf() in JavaScript
numbers = [5, 6, 7, 8, 9, 10]
numbers.index(6) #1
# you can specify the start/end, as well
numbers = [5, 5, 6, 7, 5, 8, 8, 9, 10]
numbers.index(5) #0
numbers.index(5, 1) #1
numbers.index(5, 2) #4
numbers.index(8, 6, 8) #6

# COUNT
    # return the number of times x appears in the list
numbers = [1, 2, 3, 4, 3, 2, 1, 4, 10, 2]
numbers.count(2) #3
numbers.count(21) #0

# REVERSE
    # reverse the elements in a list (in-place)
names = ["matthew", "jared", "colt"]
names.reverse()
print(names) #["colt", "jared", "matthew"]

# SORT
    # sort the items in a list (in-place)
    # EXACTLY the same thing as .sort() in JavaScript
another_list = [6, 4, 1, 2, 5]
another_list.sort()
print(another_list) #[1, 2, 4, 5, 6]

# JOIN
    # technically a string method that takes an iterable argument
    # concatenates a copy of the string between each item of the iterable
    # returns a new string
    # can be used to make sentences out of a list of words by joining on a space
words = ["Coding", "is", "fun!"]
" ".join(words)
print(words) #"Coding is fun!"

name=["Mr.", "Steele"]
". ".join(name) #"Mr. Steele"

# SLICING
    # make new lists using slices of the old list
    # [start:end:step]
# start
    # what INDEX to start slicing FROM
first_list = [1, 2, 3, 4]
first_list[1:] #[2, 3, 4]
first_list[3:] #[4]
first_list[-1:] #[4]
# end
    # what INDEX to copy up TO (exclusive counting)
first_list = -[1, 2, 3, 4]
first_list[:2] #[1, 2]
first_list[:4] #[1, 2, 3, 4]
first_list[1:3] #[2, 3]
# step
    # the number to count at atime
    # same as step with range
first_list = [1, 2, 3, 4, 5, 6]
first_list[1::2] #[2, 4, 6] => starts at index 1, increments by 2
first_list[::2] #[1, 3, 5] => has no start or end, increments by 2
first_list[1::-1] #[2, 1] => starts at index 1, decrements by 1
first_list[:1:-1] #[6, 5, 4, 3] => no start, ends up to and not including index 1, decrements by 1
first_list[2::-1] #[3, 2, 1] => starts at index 2, decrements by 1

string = "This is fun!"
string[::-1] #"fun! is This"

numbers = [1, 2, 3, 4, 5]
numbers[1:3] = ["a", "b", "c"]
print(numbers) #[1, "a", "b", "c", 4, 5]

# SWAPPING VALUES
names = ["Matthew", "Bates"]
names[0], names[1] = names[1], names[0]
print(names) #["Bates", "Matthew"]