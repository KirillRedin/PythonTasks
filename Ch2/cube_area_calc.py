"""
Program: cube_area.py
Author: Kirill Redin
Last modified: 10.11.2018
This program calculates the area of a cube's surface

Pseudocode:
length of an edge = Input length of an edge
area = 6 * length of an edge ^ 2
print area
"""

length = float(input("Enter the length of a cube's edge: "))
area = 6 * length ** 2
print("Surface area of a cube is:", area)
