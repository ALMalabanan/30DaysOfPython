# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages_set = set(ages)
print('Length of list:', len(ages))
print('Length of set:', len(ages_set))
print('The list is bigger than the set:', len(ages) > len(ages_set))

# 2. Explain the difference between the following data types: string, list, tuple and set
# String: A sequence of characters enclosed in quotes, used to represent text.
# List: An ordered, mutable collection of elements, enclosed in square brackets.
# Tuple: An ordered, immutable collection of elements, enclosed in parentheses.
# Set: An unordered, mutable collection of unique elements, enclosed in curly braces.

# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print('Number of unique words:', len(unique_words))