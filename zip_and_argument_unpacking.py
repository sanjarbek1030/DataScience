"""
***************************
ZIP AND ARGUMENT UNPACKING
***************************
"""

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# zip is lazy, so you have to do something like the following
[pair for pair in zip(list1, list2)] # is [('a', 1), ('b', 2), ('c', 3)]

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
print(letters) # ('a', 'b', 'c')
print(numbers) # (1, 2, 3)

# The asterisk (*) performs argument unpacking, which uses the 
# elements of pairs as individual arguments to zip

# works same
letters, numbers = zip(('a', 1), ('b', 2), ('c', 3))

def add(a, b): return a + b

print(add(1, 2)) # returns 3

try:
    add([1, 2]) # x = [1, 2]; y = ??? ← missing!

except TypeError:
    print("add expects two inputs")

# * is the unpacking operator
print(add(*[1, 2])) # returns 3

