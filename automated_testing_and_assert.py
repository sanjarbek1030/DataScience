"""
******************************
AUTOMATED TESTING AND ASSERT
******************************
"""

"""
try/except and assert look similar but do very different jobs. 
try/except handles errors; assert creates one on purpose.
"""

assert 1 + 1 == 2
assert 1 + 1 == 2, "1 + 1 should equal 2 but didn't"

def smallest_item(xs):
    return min(xs)

assert smallest_item([10, 20, 5, 40]) == 5
assert smallest_item([1, 0, -1, 2]) == -1

def smallest_item2(xs):
    assert xs, "empty list has no smallest item"
    return min(xs)

