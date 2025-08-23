# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
def calculate_y(x):
    return x**2 + 6*x + 9

# Try different x values
for x in range(-10, 11):
    y = calculate_y(x)
    print(f"For x = {x}, y = {y}")
    if y == 0:
        print(f"y is 0 when x = {x}")

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python_length = len('python')
dragon_length = len('dragon')
print(f"Length of 'python': {python_length}")
print(f"Length of 'dragon': {dragon_length}")
print(f"Is 'python' longer than 'dragon'? {python_length > dragon_length}")

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print(f"Is 'on' found in both 'python' and 'dragon'? {'on' in 'python' and 'on' in 'dragon'}")
