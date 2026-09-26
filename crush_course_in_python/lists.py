"""
****************
LISTS
****************
"""

integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []] # 3 ta list

list_length = len(integer_list)
list_sum = sum(integer_list)

# print(list_length)
# print(list_sum)

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("x: ", x)

zero = x[0]
one = x[1]
nine = x[-1]
eight = x[-2]

x[0] = -1 # [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]

first_three = x[:3] # [-1, 1, 2]
three_to_end = x[3:] # [3, 4, 5, 6, 7, 8, 9]
one_to_four = x[1:5] # [1, 2, 3, 4]
last_three = x[-3:] # [7, 8, 9]
without_first_and_last = x[1:-1] # [1, 2, 3, 4, 5, 6, 7, 8]

every_third = x[::3] # [-1, 3, 6, 9]
five_to_three = x[5:2:-1] # [5, 4, 3]

one_in_x = 1 in x
zero_in_x = 0 in x

# print("one_in_x: ", one_in_x)
# print("zero_in_x: ", zero_in_x)

x = [1, 2, 3]
x.extend([4, 5, 6]) # x is now [1, 2, 3, 4, 5, 6]. x is modified

x = [1, 2, 3]
y = x + [4, 5, 6] # y is [1, 2, 3, 4, 5, 6] and x is unchanged

x = [1, 2, 3]
x.append(0) # x = [1, 2, 3, 0]
y = x[-1]  # y is 0
z = len(x) # equals 4

x, y = [1, 2] # unpacking list, now x is 1, y is 2

_, y = [1, 2] # now y == 2, didn't care about first element

