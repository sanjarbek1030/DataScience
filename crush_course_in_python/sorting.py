"""
****************
SORTING
****************
"""

x = [4, 1, 2, 3]
y = sorted(x) # y is [1, 2, 3, 4], x is unchanged
x.sort() # now x is [1, 2, 3, 4]

# sort the list by absolute value from largest to smallest
x = sorted([-4, 1, -2, 3], key=abs, reverse=True) # is [-4, 3, -2, 1]

# sort the words and counts from highest count to lowest
word_counts = {}
wc = sorted(word_counts.items(), # .item() equals tuple (word, count)
            key=lambda word_and_count: word_and_count[1], # tuple is named word_and_count, [1] returns count
            reverse=True)
