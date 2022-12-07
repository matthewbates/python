
#* SYNTAX
# [___ for ___ in ___]
nums = [1, 2, 3]
print([x * 2 for x in nums])

# examples
[num * 10 for num in range(1, 6)] #[10, 20, 30, 40, 50]

name = "matthew"
[char.upper() for char in name] #["M", "A", "T", "T", "H", "E", "W"]

[bool(val) for val in [0, [], ""]] #[False, False, False]

# converting one data type to another (number to string)
numbers = [1, 2, 3, 4, 5]
string_list = [str(num) for num in numbers] #["1", "2", "3", "4" ,"5"]

#* LIST COMPREHENSION WITH CONDITIONAL LOGIC
numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num != 0]
[num * 2 if num % 2 == 0 else num / 2 for num in numbers] #[0.5, 4, 1.5, 8, 2.5, 12]

with_vowels = "This is so much fun!"
"".join(char for char in with_vowels if char not in "aeiuo") #"Ths s s mch fn!"

