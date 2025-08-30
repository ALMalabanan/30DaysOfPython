#Accessing Tuple Items
# Syntax
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]
print('First Item:', first_item)
print('Second Item:', second_item)

#Negative Indexing
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
print('First Fruit:', first_fruit)
print('Second Fruit:', second_fruit)
print('Last Fruit:', last_fruit)

#Slicing Tuples
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3
print('All Items:', all_items)
print('Middle Two Items:', middle_two_items)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]
print('All Fruits:', all_fruits)
print('Orange and Mango:', orange_mango)
print('Orange to the Rest:', orange_to_the_rest)

#Range of Negative Indexes
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]
print('All Fruits:', all_fruits)
print('Orange and Mango:', orange_mango)
print('Orange to the Rest:', orange_to_the_rest)

#Changing Tuple to List
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')

#Checking an Item in a Tuple
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
# fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment

# Joining Tuples
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
print('Joined Tuple:', tpl3)

# Deleting Tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
#print(fruits) # NameError: name 'fruits' is not defined

