#The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print('All Ages:', ages)


# Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print('Sorted Ages:', ages)
print('Min Age:', min_age)
print('Max Age:', max_age)

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print('Ages after adding min and max:', ages)

# Find the median age (one middle item or two middle items divided by two)
if len(ages) % 2 == 0:
    median_age = (ages[len(ages) // 2 - 1] + ages[len(ages) // 2]) / 2
else:
    median_age = ages[len(ages) // 2]
print('Median Age:', median_age)

# Find the average age (sum of all items divided by their number )
average_age = sum(ages) / len(ages)
print('Average Age:', average_age)