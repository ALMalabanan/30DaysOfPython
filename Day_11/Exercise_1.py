# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(3, 5)) # 8

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(radius):
    PI = 3.14
    area = PI * radius * radius
    return area
print(area_of_circle(5)) # 78.5

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    if not all(isinstance(i, (int, float)) for i in args):
        return "All arguments must be numbers."
    return sum(args)
print(add_all_nums(1, 2, 3, 4.5)) # 10.5
print(add_all_nums(1, '2', 3)) # All arguments must be numbers.

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(convert_celsius_to_fahrenheit(0)) # 32.0
print(convert_celsius_to_fahrenheit(100)) # 212.0

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Invalid month"
print(check_season(3)) # Spring
print(check_season(11)) # Autumn
print(check_season(13)) # Invalid month
print(check_season(7)) # Summer
print(check_season(1)) # Winter


# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Slope is undefined (vertical line)"
    slope = (y2 - y1) / (x2 - x1)
    return slope
print(calculate_slope(1, 2, 3, 4)) # 1.0
print(calculate_slope(2, 3, 2, 5)) # Slope is undefined (vertical line)

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
import cmath
def solve_quadratic_eqn(a, b, c):
    d = (b**2) - (4*a*c)  # discriminant
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    return (sol1, sol2)
print(solve_quadratic_eqn(1, -3, 2)) # ((1+0j), (2+0j))
print(solve_quadratic_eqn(1, 2, 5)) # ((-1-2j), (-1+2j))

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for item in lst:
        print(item)
print_list([1, 2, 3, 'a', 'b'])
# 1
# 2

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(arr):
    reversed_arr = []
    for item in arr:
        reversed_arr.insert(0, item)
    return reversed_arr
print(reverse_list([1, 2, 3, 4, 5])) # [5, 4, 3, 2, 1]
print(reverse_list(['a', 'b', 'c'])) # ['c', 'b', 'a']


