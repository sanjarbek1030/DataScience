"""
****************
CONTROL FLOW
****************
"""

if 1 > 2:
    message = "if only 1 were greater than two"
elif 1 > 3:
    message = "elif stands for else if"
else:
    message = "when all else fails use else (if you want to)"

x = 10

# ternary expression
parity = "even" if x % 2 == 0 else "odd"
#         ↑            ↑              ↑
#    value if TRUE   condition   value if FALSE


# While Loop
x = 0
while x < 10:
    print(f"{x} is less than 10")
    x += 1 

# range(10) is the numbers 0, 1, ..., 9
for x in range(10):
    print(f"{x} is less than 10")

for x in range(10):
    if x == 3:
        continue # go immediately to the next iteration
    if x == 5:
        break
    print(x)

