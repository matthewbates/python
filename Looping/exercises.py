
#* EXERCISE 1
times = input("How many times do I have to tell you? ")
times = int(times)

for time in range(times):
    print(" CLEAN UP YOUR ROOM")

#* EXERCISE 2
# loop through numbers 1-20 (remember 20 is exclusive)
# for 4 and 13, print "x is unlucky"
# for even numbers, print "x is even"
# for odd numbers, print "x is odd"

for num in range(1, 21):
    if num == 4 or num == 13:
        print(f"{num} is unlucky")
    elif num % 2 == 0:
        print(f"{num} is even")
    else: 
        print(f"{num} is odd")

# refactored version
for num in range(1, 21):
    if num == 4 or num == 13:
        state = "unlucky"
    elif num % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{num} is {state}")

#* EXERCISE 3
for num in range(1, 11):
    print("\U0001f600" + num)

# basic solution
times = 1
while times < 11:
    print("\U0001f600" + times)
    times += 1

# alternative solution, w/o string multiplication
for num in range(1, 11):
    count = 1
    smileys = ""
    while count <= num:
        smileys += "\U0001f600"
        count += 1
    print(smileys)

#* EXCERCISE 4
msg = input("Say something: ")
while msg != "stop copying me":
    print(msg)
    msg = input()
print("UGH FINE YOU WIN")

#* EXERCISE 5 (REVISITING EXERCISE 1)
times = int(input("How many times do I have to tell you? "))
for time in range(times):
    print("CLEAN YOUR ROOM!")
    if time >= 4:
        print("Do you even listen anymore?")
        break