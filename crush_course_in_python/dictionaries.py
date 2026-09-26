"""
****************
DICTIONARIES
****************
"""
from collections import defaultdict


empty_dict = {}
empty_dict2 = dict()
grades = {"Luffy": 80, "Zoro": 90}

luffys_grade = grades["Luffy"] # equals 80
print("Luffy's grade: ", luffys_grade)

try:
    namis_grade = grades["Nami"]
except KeyError:
    print("no grade for Nami!")

luffy_has_grade = "Luffy" in grades # True
nami_has_grade = "Nami" in grades # False

luffy_has_grade = grades.get("Luffy", 0) # equals 80
nami_has_grade = grades.get("Nami", 0) # eqauls 0
no_ones_grade = grades.get("No One") # default is None

grades["Usopp"] = 85
grades["Sanji"] = 95
num_students = len(grades)

tweet = {
    "user": "monkeydluffy",
    "text": "Data Science is awesome!",
    "retweet_count": 100,
    "hashtags": ["#data", "#science", "#datascience", "#yolo"]
}

tweet_keys = tweet.keys() # iterable for the keys; storing all keys into single var
tweet_values = tweet.values() # iterable for the values
tweet_items = tweet.items() # iterable for the (key, value) tuples

"user" in tweet_keys # True, but not Pythonic (not easy to read)
"user" in tweet # Pythonic way of checking for keys
"monkeydluffy" in tweet_values # True (slow but only way to check)

# defaultdict
document = ["a", "b", "a"]
word_counts= {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1


word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1


word_counts = defaultdict(int)
for word in document:
    word_counts[word] += 1


dd_list = defaultdict(list) # list() produces an empty list
dd_list[2].append(1) # now dd_list contains {2: {1}}

dd_list = defaultdict(dict) # dict() produces an empty list
dd_list["Joel"]["City"] = "Seattle" # {"Joel": {"City": "Seattle"}}

dd_pair = defaultdict(lambda: [0, 0]) 
dd_pair[2][1] = 1 # now dd_pair contains {2: [0, 1]}
