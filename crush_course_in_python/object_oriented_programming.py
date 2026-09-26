"""
*****************************
OBJECT-ORIENTED PROGRAMMING
*****************************
"""

"""
__init__ method, “magic” method, also called “dunder”
method (double-UNDERscore), represents “special” behaviors.
"""

class CountingClicker:
    """A class can/should have docstring, just like a function"""

    def __init__(self, count=0):
        self.count = count

    def __repr__(self):
        return f"CountingClicker(count={self.count})"
    
    def click(self, num_times = 1):
        """Click the clicker some number of times."""
        self.count += num_times
    
    def read(self):
        return self.count
    
    def reset(self):
        self.count = 0

clicker1 = CountingClicker() # initialized to 0
clicker2 = CountingClicker(100) # starts with count=100
clicker3 = CountingClicker(count=100) # more explicit way of doing the same

clicker = CountingClicker()
assert clicker.read() == 0, "clicker should start with count 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "after two clicks, clicker should have count 2"
print("after two click: ", clicker.read())
clicker.reset()
assert clicker.read() == 0, "after reset, clicker should be back to 0"

# A subclass inherits all the behavior of its parent class
class NoResetClicker(CountingClicker):
    # This class has all the same methods as CountingClicker
    # Except that it has reset method that does nothing.
    def reset(self):
        pass

no_reset_clicker = NoResetClicker() # initialized to 0
assert no_reset_clicker.read() == 0 # clicker should start with count 0
no_reset_clicker.click()
assert no_reset_clicker.read() == 1 # clicker should have count 1
no_reset_clicker.reset()
assert no_reset_clicker.read() == 1 # reset shouldn't do anything

print("reset not working: ", no_reset_clicker.read())



