age= 23
height = 1.71
cmplx= 1 + 2j

# Calculate the area of a triangle
print('Enter base: ')
base = float(input())
print('Enter height: ')
height = float(input())
print('Area of this triangle is: ', 0.5 * base * height)

#Calculate the Perimeter of a triangle
print('Enter side a: ')
a = float(input())
print('Enter side b: ')
b = float(input())
print('Enter side c: ')
c = float(input())
print('Perimeter of this triangle is: ', a + b + c)

#Getting the area and perimeter of a triangle with length and width
print('Enter length: ')
length = float(input())
print('Enter width: ')
width = float(input())
print('Area of this rectangle is: ', length * width)
print('Perimeter of this rectangle is: ', 2 * (length + width))

#Getting the radius of circle
pi=3.14
print('Enter radius: ')
radius = float(input())
print('Area of this circle is: ', pi * radius**2)
print('Circumference of this circle is: ', 2 * pi * radius)

#Calculating the slope, x-intercept and y intercept of y = 2x -2
print('For the equation y = 2x -2')
print('Slope (m) = 2')
print('Y-intercept (b) = -2')
print('X-intercept = 1')

#slope is (m = y2-y1/x1-x1) Find the slope and euclidean distance between point (2,2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
euclidean_distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print('Slope (m) =', slope)
print('Euclidean distance =', euclidean_distance)
