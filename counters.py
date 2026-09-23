"""
****************
Counters
****************
"""
from collections import Counter

c = Counter([0, 1, 2, 0]) # c is (basically) {0: 2, 1: 1, 2: 1}

document = {"a", "b", "a"}

# recall, document is a list of words
word_counts = Counter(document)

# print the 10 most common words and their counts
for word, count in word_counts.most_common(10):
    print(word, count)

