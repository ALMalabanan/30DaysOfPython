#Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
print(type(-1)) #int
print(type(3.14)) #float
print(type(1 + 2j)) #Complex Number
print(type('Hello World')) #string
print(type(False)) #boolean
print(type([1, 2, 3])) #list
print(type((1, 2, 3))) #tuple
print(type({1, 2, 3})) #set
print(type({'name': 'Angelo', 'country': 'Philippines'})) #dictionary


#Find an Euclidian distance between (2, 3) and (10, 8)
import math

# Points coordinates
x1, y1 = 2, 3 #first point
x2, y2 = 10, 8 #second point

# Calculate the Euclidean distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(distance)