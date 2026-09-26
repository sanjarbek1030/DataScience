"""
****************
TRUTHINESS
****************
"""
one_is_less_than_two = 1 < 2 # equals True
true_equals_false = True == False # equals False

x = None
assert x == None, "this is the not Pythonic way to check for None"
assert x is None, "this is the Pythonic way to check for None"

# falsy: False, None, [] (an empty list), {} (an empty dict), "", set(), 0, 0.0
# truthy: Pretty much anything else

def some_function_that_returns_a_string():
    (...)

s = some_function_that_returns_a_string()
if s:
    first_char = s[0]
else:
    first_char = ""

first_char = s and s[0] # if left falsy return left, if left truthy return right

safe_x = x or 0

safe_x = x if x is not None else 0

all([True, 1, {3}]) # True, all are truthy
all([True, 1, {}]) # False, {} is falsy
any([True, 1, {}]) # True, True is truthy
all([]) # True, no falsy elements in the list, does not check list, checks inside of list
any([]) # False, no truthy elements in the list
