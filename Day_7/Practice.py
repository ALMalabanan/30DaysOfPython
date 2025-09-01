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
print(st)