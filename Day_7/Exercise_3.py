# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages_set = set(ages)
print('Length of list:', len(ages))
print('Length of set:', len(ages_set))
print('The list is bigger than the set:', len(ages) > len(ages_set))