# handle user guesses
    # if they guess correct, tell them they won. Otherwise, tell them if they are too high or too low
#* VERSION 1
# import random
# random_number = random.randint(1, 10)
# guess = None

# while guess != random_number:
#     guess = input("Pick a between from 1 to 10: ")
#     guess = int(guess)
#     if guess < random_number:
#         print("TOO LOW!")
#     elif guess > random_number:
#         print("TOO HIGH!")
#     else:
#         print("YOU WON!")
# print(random_number)

#* VERSION 2
import random
random_number = random.randint(1, 10)
guess = None

while guess != random_number:
    guess = input("Pick a number between 1 and 10: ")
    guess = int(guess)
    if guess < random_number:
        print("Too low!")
    elif guess > random_number:
        print("Too high!")
    else:
        print("You won!")
        play_again = input("Would you like to play again? (y/n)")
        if play_again == "y":
            random_number = random.randint(1, 10)
            guess = None
        else:
            print("Thank you for playing!")
            break