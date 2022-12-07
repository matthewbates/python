
#* NESTED LISTS
# lists can contain any jkind of element, even other lists
# complex data structures - matricies
# game boards / mazes

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nested_list[0][1] #2 => first list, then index 1 in first list
nested_list[1][-1] #6 => second list, last index in second list

for l in nested_list:
    for val in l:
        print(val) #1, 2, 3, 4, 5, 6, 7, 8, 9