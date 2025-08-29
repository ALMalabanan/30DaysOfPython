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