# Creating and checking the length of a set
st = {'item1', 'item2', 'item3', 'item4'}
print(len(st))

# Checking if an item exists in a set
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True
print("Does set st contain item5? ", 'item5' in st) # Does set st contain item5? False

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('Does set fruits contain mango? ', 'mango' in fruits ) # True

# Adding Items to a set
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)

# Adding Multiple Items using Update()
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
print('Adding Multiple Items using Update:' , st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print('Adding Multiple Items using Update:', fruits)

# Removing Items from a set
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
print('Removing Items from a set:', st)

#Remove Random Item 
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set
print('Removing Random Item:', fruits)

# Clearing Items in a Set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print("Clearing Items in a set:", fruits) # set()

# Deleting a Set
#fruits = {'banana', 'orange', 'mango', 'lemon'}
#del fruits
#print("Deleting a set:", fruits) # NameError: name 'fruits' is not defined

# Converting List to Set
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
print('Converting List to Set:', fruits)

# Joining Sets
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print('Joining Sets:', fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print('Adding Vegetables to fruits:', fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}