# While Loop
count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4

# Break and Continue
count = 0
while count < 5:
    print('Counts 0-2', count)
    count = count + 1
    if count == 3:
        break

# Other Way
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print('Counts 0-4', count)
    count = count + 1
# Skips 3 and prints 0,1,2,4

# For Loop
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5

# Other Way
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

# For Loop with Tuple
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# For Loop with Dictionary
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out