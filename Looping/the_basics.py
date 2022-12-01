
#* LOOPING BASICS
# syntax:
# for item in iterable_object:
    # do something with item

# an iterable object is some kind of collection of items, for instance: a list of numbers, a string of characters, a range, etc.
# item is a new variable that can be called whatever you want
# item references the current position of our iterator with the iterable. It will iterate over (run through) every item of the collection and then go away when it has visited all items

for char in "hello":
    print(char)

#* FOR LOOPS WITH RANGES
for number in range(1, 8):
    print(number)

# if we just want to print numbers, we can simply iterate over a range
# range(7) gives you integers from 0 through 6 - THIS IS EXCLUSIVE
# range(1, 10, 2) will give you odds from 1  to 10
    # 1, 3, 5, 7, 9
# range(1, 8) will give you integers from 1 to 7
# range(7, 0, -1) will give you integers from 7 to 1
    # 7, 6, 5, 4, 3, 2, 1

# if you want to see the range, use list()
r = range(10)
list(r)

#* FOR LOOP AND RANGE EXERCISE
# use a for loop to add up every odd number from 10 to 20 (inclusive) and store the result in variable x
x = 0

for n in range(10, 21):
    if n % 2 != 0:
        x += n

#* WHILE LOOPS
# while loops continue to execute while a certain condition is truthy, and will end when they become falsy
# you have to specify the termination conditions manually
msg = input("What's the secret password? ")
while msg != "bananas":
    print("WRONG!")
    msg = input("What's the secret password?")
print("CORRECT!")

num = 1
while num < 11:
    print(num)
    num += 1

#* CONTROLLED EXIT
# the keyword breat gives us the ability to exit out of while loops whenever we want
# used with a while loop:
while True:
    command = input("Type 'exit' to exit: ")
    if (command == "exit"):
        break

# used with a for loop:
for x in range(1, 101):
    print(x)
    if x == 3:
        break