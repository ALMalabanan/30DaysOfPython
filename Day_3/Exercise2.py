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

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print(f"Is 'jargon' found in the sentence? {'jargon' in 'I hope this course is not full of jargon.'}")

#There is no 'on' in both dragon and python
print(f"Is 'on' found in both 'dragon' and 'python'? {'on' in 'dragon' and 'on' in 'python'}")

#Find the length of the text python and convert the value to float and convert it to string
python_length_float = float(python_length)
dragon_length_float = float(dragon_length)
print(f"Length of 'python' as float: {python_length_float}")
print(f"Length of 'dragon' as float: {dragon_length_float}")
print(f"Length of 'python' as string: {str(python_length_float)}")
print(f"Length of 'dragon' as string: {str(dragon_length_float)}")

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input("Enter a number to check if it's even or odd: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(f"Is the floor division of 7 by 3 equal to the int converted value of 2.7? {7 // 3 == int(2.7)}")\

#Check if type of '10' is equal to type of 10
print(f"Is the type of '10' equal to the type of 10? {type('10') == type(10)}")

#Check if int('9.8') is equal to 10
print(f"Is int('9.8') equal to 10? {int(9.8) == 10}")

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter hours worked: "))
rate = float(input("Enter rate per hour: "))
pay = hours * rate
print(f"Total pay: {pay}")

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = float(input("Enter number of years: "))
seconds = years * 365 * 24 * 60 * 60
print(f"Total seconds lived: {seconds}")

# Write a Python script that displays the following table 
#1 1 1 1 1
#2 1 2 4 8
#3 1 3 9 27
#4 1 4 16 64
#5 1 5 25 125

print("Number\t1\tN\tN^2\tN^3")  # Header
for n in range(1, 6):
    print(f"{n}\t{1}\t{n}\t{n**2}\t{n**3}")