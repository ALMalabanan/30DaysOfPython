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