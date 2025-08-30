# Create an empty tuple
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

#Create a tuple containing names of your "sisters" and your "brothers" (imaginary siblings are fine)
sisters = ('Anna', 'Beth', 'Cathy')
brothers = ('David', 'Ethan', 'Frank')

# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print('Siblings:', siblings)

# How many siblings do you have?
print('Number of siblings:', len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Juan', 'Maria')
print('Family members:', family_members)

# Unpack siblings and parents from family_members
siblings = family_members[:len(sisters) + len(brothers)]
parents = family_members[len(siblings):]
print('Siblings:', siblings)
print('Parents:', parents)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'cherry')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'cheese', 'yogurt')
food_stuff_tp = fruits + vegetables + animal_products
print('Food stuff:', food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print('Food stuff list:', food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_tp) // 2
if len(food_stuff_tp) % 2 == 0:
    middle_items_tp = food_stuff_tp[middle_index - 1:middle_index + 1]
    middle_items_lt = food_stuff_lt[middle_index - 1:middle_index + 1]
else:
    middle_items_tp = (food_stuff_tp[middle_index],)
    middle_items_lt = [food_stuff_lt[middle_index]]

print('Middle item(s) in tuple:', middle_items_tp)
print('Middle item(s) in list:', middle_items_lt)

# Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print('First three items:', first_three_items)
print('Last three items:', last_three_items)

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
print('apple' in food_stuff_lt)

# Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia is a Nordic country:', 'Estonia' in nordic_countries)

# Check if 'Iceland' is a nordic country
print('Iceland is a Nordic country:', 'Iceland' in nordic_countries)