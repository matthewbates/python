print("How many kilometers did you cycle today?")
# this takes a prompt which is a STRING value
kms = input()
miles = float(kms)/1.60934
# round(thing to round, how many decimal places)
miles = round(miles, 2)
# alternatively, it could be:
# print(f"That is equal to {round(miles, 2)} miles")
print(f"That is equal to {miles} miles")