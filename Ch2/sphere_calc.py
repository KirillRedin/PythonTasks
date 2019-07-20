"""
Program: sphere_calc.py
Author: Kirill Redin
Last modified: 10.11.2018
This program is calculating sphere diameter, circumference,
surface area and volume

Pseudocode:
sphere radius = Input sphere radius
sphere diameter = sphere radius * 2
sphere circumference = pi * sphere diameter
sphere area = pi * sphere diameter ^ 2
sphere volume = 4 / 3 * pi * sphere radius ^ 3
print sphere diameter, sphere circumference, sphere area, sphere volume
"""

import math

sphere_radius = float(input("Enter sphere radius: "))
sphere_diameter = sphere_radius * 2
sphere_circumference = math.pi * sphere_diameter
sphere_area = math.pi * sphere_diameter ** 2
sphere_volume = math.pi * 4 / 3 * sphere_radius ** 3
print("Sphere diameter is:", sphere_diameter, "\nSphere circumference is:", \
      sphere_circumference, "\nSphere area is:", sphere_area,\
      "\nSphere volume is:", sphere_volume)
