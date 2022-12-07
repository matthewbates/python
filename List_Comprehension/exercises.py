
#* EXERCISES
# given a list ["Elie", "Tim", "Matt"], create a variable called answer, which is a new list containing the first leter of each name in the list
answer = [char[0] for char in ["Elie", "Tim", "Matt"]] #["E", "T", "M"]

# given a list [1, 2, 3, 4, 5, 6], create a variable called answer2, which is a new list of all the even values
answer2 = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0] #[2, 4, 6]

# given two lists [1, 2, 3, 4] and [3, 4, 5, 6], create a variable called answer, which is a new list that is the intersection of the two. The output should be [3, 4]
answer = [val for val in [1, 2, 3, 4] if val in [3, 4, 5, 6]] #[3, 4]

# given a list of words ["Elie", "Tim", "Matt"], create a variable called answer2, which is a new list with each word reversed and in lower case
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]] #["eile", "mit", "ttam"]

# for all the numbers between 1 and 100 (including 100), create a variable called answer, which contains a list with all the numbers that are divisible by 12
answer = [num for num in range(1, 101) if num % 12 == 0]

# given the string "amazing", create a variable called answer, which is a list containing all the letters from "amazing" but not the vowels
answer = [char for char in "amazing" if char not in "aeiou"]

# using a nested list comprehension and range(), create a variable called answer with the following value - [[0, 1, 2], [0, 1, 2], [0, 1, 2]]. Start by using range and a list comp to generate the list [0, 1, 2] and then repeat that whole thing 3 times in a nested list comp
answer = [[i for i in range(0, 3)] for num in range(0, 3)]