import re as regex
import matplotlib.pyplot as plt
import math
import this

print(this)

# The pound sign marks the start of a comment. Python itself
# ignores the comments, but they're helpful for anyone reading the code

#for i in [1, 2, 3, 4, 5]:
#    print(i)
#    for j in [1, 2, 3, 4, 5]:
#        print(i)
#        print(i + j)
#    print(i)
#print("done looping")

"""
*********
INTENDATION (JOY TASHLASH)
*********
"""
# whitespace is ignored inside (), []
long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 
                           8 + 9 + 10 + 11 + 12 + 13 + 14 + 
                           15 + 16 + 17 + 18 + 19 + 20)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

easier_to_read_list_of_lists = [[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]]

# we can use backslash to continue onto the next line
two_plus_three = 2 + \
                 3


#print(long_winded_computation)
#print(easier_to_read_list_of_lists)
#print(two_plus_three)


my_regex = regex.compile("[0-9]+", regex.I)
#print(my_regex)

"""
*********
FUNCTIONS
*********
"""

# single line comment
# men
# dasturchiman



def double(x): # bu funksiya
    """
    This is where you put an optional docstring that explains what
    the function does. For example, this function multiplies its
    input by 2
    """
    return x * 2

def apply_to_one(f):
    """Calls the function f with 1 as its argument"""
    return f(1)

my_double = double
x = apply_to_one(my_double)

y = apply_to_one(lambda x: x + 4) # equals 5


def my_print(message = "my default message"):
    print(message)


def full_name(first="What's-his-name", last="Something"):
    return first + " " + last


print(double(2))
print(x)
print(y)
my_print("Hello, World!")
my_print()
print(full_name("Joel", "Grus"))
print(full_name("Joel"))
print(full_name(last="Grus"))

"""
******
STRING
******
"""

single_quoted_string='data science'
double_quoted_string="data science"

tab_string = "\t" # represents the tab character
#print(len(tab_string)) # is 1

not_tab_sting = r"\t" # represents the characters '\' and 't'
#print(len(not_tab_sting)) # is 2

multi_line_sting = """This is the first line.
and this is the second line
and this is the third line"""


first_name = "Joel"
last_name = "Grus"
full_name1 = first_name + " " + last_name
full_name2 = "{0} {1}".format(first_name, last_name)


full_name3 = f"{first_name} {last_name}"

# print(full_name1)
# print(full_name2)
# print(full_name3)

"""
**************
EXCEPTIONS
**************
"""

# try:
#     print(0 / 0)
# except ZeroDivisionError:
#     print("cannot divide by zero")


"""
****************
LISTS/ARRAY
****************
"""

integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []] # 3 ta list

list_length = len(integer_list)
list_sum = sum(integer_list)

print(list_length)
print(list_sum)

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x)

zero = x[0]
one = x[1]
nine = x[-1]
eight = x[-2]

x[0] = -1 # [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x[9] = -10 # [-1, 1, 2, 3, 4, 5, 6, 7, 8, -10]
print(x)


"""
****************
TUPLES/LISTS
****************
"""

my_list = [1, 2]

my_tuple = (1, 2) # o'zgarmas

other_tuple = 3, 4

my_list[1] = 3 # my_list is now [1, 3]

# Error handling
try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a tuple")


"""
****************
DICTIONARIES/Objects {key: value, key: value...}
****************
"""

empty_dict = {}# Pythonic

empty_dict2 = dict() # less Pythonic dict degan metod bilan

grades = {"Joel": 80, "Tim": 95} # dictionary literal

joels_grade = grades["Joel"]
print(joels_grade)

try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!")

joel_has_grade = "Joel" in grades # True
kate_has_grade = "Kate" in grades # False


"""
****************
SETS
****************
"""
primes_below_10 = {2, 3, 5, 7}

s = set()

s.add(1) # s is now {1}
s.add(2) # s is now {1, 2}
s.add(2) # s is still {1, 2}

x = len(s) # equals 2

y = 2 in s # equals True
z = 3 in s # equals False

