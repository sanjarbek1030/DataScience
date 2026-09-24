"""
*************************
ITERABLES AND GENERATORS
*************************
"""

def generate_range(n):
    i = 0
    while i < n:
        yield i # every call to yield produces a value of the generator
        i += 1

print("generate_range: ", generate_range(5))

for i in generate_range(5):
    print(f"i: {i}")


def natural_numbers():
    """returns 1, 2, 3, ..."""
    n = 1
    while True:
        yield n
        n += 1


evens_below_20 = (i for i in generate_range(20) if i % 2 == 0)


# None of these computations *does* anything until we iterate
data = natural_numbers()
evens = (x for x in data if x % 2 == 0)
even_squares = (x ** 2 for x in evens)
even_squares_ending_in_six = (x for x in even_squares if x % 10 == 6)
# and so on


names = ["Alice", "Bob", "Charlie", "Debbie"]

# not Pythonic
for i in range(len(names)):
    print(f"name {i} is {names[i]}")

# also not Pythonic
i = 0
for name in names:
    print(f"name {i} is {names[i]}")
    i += 1

# Pythonic
for i, name in enumerate(names):
    print(f"name {i} is {name}")

