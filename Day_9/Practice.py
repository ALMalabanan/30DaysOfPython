# If Condition
a = 3
print("Value of a:", a)
if a > 0:
    print('A is a positive number')
else:
    print('A is a negative number')
# A is a positive number

# If Elif Else
a = 0
print('Value of A:', a)
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

#Short Hand
a = 3
print('Value of A:', a)
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed

#Nested Conditions
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
