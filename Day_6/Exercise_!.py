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