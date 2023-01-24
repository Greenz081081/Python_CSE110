# File: Third assignment.py
# Purpose: Using variable and expressions for straight-forward
# math calculations

# Author: Emediong Edet.
square = float(input('What is the length of a side of the square?'))
area_1 = square ** 2
print(f'The area of the square is {area_1}')
print()
rectangle_length = float(input('What is the length of rectangle?'))
rectangle_width = float(input('What is the width of the rectangle?'))
area_2 = rectangle_length * rectangle_width
print(f'The area of the rectangle is {area_2}')
print()
circle = float(input('What is the radius of the circle?'))
area_3 = 3.1416 * (circle ** 2)
print(f'The area of the circle is {area_3}.')
print()
# Strecth Part of the Assignment

import math
radius = float(input('What is the radius of a circle?'))
area_4 = math.pi * (radius ** 2)
print(f'The area of the circle is {area_4}')

value = float(input('What value is to be used?'))
print()
print()
area_circle = math.pi * (value ** 2)
area_square = value ** 2
volume_cube = value ** 3
volume_sphere = (4 / 3) * math.pi * (value ** 3)
print()
print(f'The area of a circle is {area_circle}')
print(f'The area of the square is{area_square}')
print(f'The volume of the cube is {volume_cube}')
print(f'The the volume of the sphere is {volume_sphere}')
print()
# Strecth 3: cm 2 m
print('Area of a square')
side = float(input('What is the legnth of a side of the square in ( cm )? '))
print()
print()
area = side ** 2
print()
print(f'The length of the square is: {area} cm^2')
print(f'The legnth of the square is: {area / 10000} m^2')
print()
print('Area of a rectangle')
length = float(input('What is the length of a rectangle (in cm)?'))
width = float(input('What is the width of a rectangle (in cm)?'))
area = length * width
print(f'The length of a rectangle is: {area} cm^2')
print(f'The width of a rectangle is: {area / 10000} m^2')

print()
print('Area of a circle')
radius = float(input('What is the radius of the circle in ( cm )'))
area = 3.1416 * radius
print(f'The area of the circle is: {area} cm^2')
print(f'The area of the circle is: {area / 10000} m^2')
print()
end = float(input('_____________________________'))
