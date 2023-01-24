# Week 04 Team assignment
# Purpose: Write a program determining how fast an object will fall.
# Author: Team 07

import math 

print()
print("---------------------------------------------")
print()
print("Formula: v(t) sqrt(mg/c) * (1 - exp(( - sqrt(mgc/m) t)")
print()
print("Welcome to the volocity calculator: Please enter the following information:")


mass = float(input("Mass (in kg):"))
gravity = float(input("Gravity (in m/s^2, 9.8 for earth, 24 for jupiter):"))
time = float(input("Time (in seconds):"))
density = float(input("Density of fluid (in m/s^3, 1.3 for air, 1000 for water):"))
area_of_projection = float(input("Cross sectional area (in m^2):"))
drag_constant = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder):"))


print()
value_of_C = (1 / 2) * density * area_of_projection * drag_constant

print()
print(f"The inner value of C is: {value_of_C :.3f} ")

sub_velocity = math.sqrt(mass * gravity / value_of_C) * (1 - math.exp((-math.sqrt(mass * gravity * value_of_C) / mass) * time))
print(f"The velocity after 10.0 seconds is: {sub_velocity :.3f} m/s")

print()
print("-----------------------------------------------")
end = input("..")