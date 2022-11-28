
#*LOGICAL OPERATORS
# in Python, the following operators can be used to make boolean logic comparisons or statements:

# and ==> truthy if BOTH a AND b are true
age = 6
age > 2
print(age > 2 and age < 8) #True
print (age > 6 and age < 8) #False

# or ==> truthy if EITHER a OR b are true]
city = input("Where do you live? ")
if city == "Los Angeles" or city == "San Francisco":
    print("You live in California!")
else:
    print("You live somewhere else!")

print(1 < 3 or 1 == 99)

# not ==> truty if the OPPOSITE of a is true
age = 10
print(age < 4) #False
print(not age < 4) #True

age = 21
# 2-8 dollar ticket
# 65 5 dollar ticket
# 10 dollars for everyone else
              #false          or   #false
if not((age >= 2 and age <=8) or age >= 65):
    print("You pay 10 dollars and are not a child or senior!")
else:
    print("You are a child or senior!") 