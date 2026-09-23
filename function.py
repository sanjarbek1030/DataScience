"""
*********
FUNCTIONS
*********
"""

# single line comment

"""
multiple
line
comment
"""


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
