# ask for age
age = input("Please enter your age: ")
# if the user just hits enter without entering an age, it will return an error
if age:
    # 18-21 need a wristband
    age = int(age)
    if age >= 18 and age < 21:
        print("You can enter, but need a wristband!")
    # 21+ to drink, normal entry
    elif age >= 21:
        print("You're good to enter and you can drink!")
    # all other cases, return the following:
    else:
        print("You can't come in, little one! :(")
else:
    print("Please enter an age!")