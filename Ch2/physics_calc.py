"""
Program: physics_calc.py
Author: Kirill Redin
Last modified: 10.11.2018
This program calculates object's momentum and kinetic energy
using it's mass and velocity

Pseudocode:
mass = Input object's mass
velocity = Input object's velocity
momentum = mass * velocity
kinetic energy = mass * velocity ** 2 / 2
print momentum
"""

mass = float(input("Enter object's mass: "))
velocity = float(input("Enter object's velocity: "))
momentum = mass * velocity
kinetic_energy = mass * velocity ** 2 / 2
print("Object's momentum =", momentum, "\nObject's kinetic energy =", \
      kinetic_energy)
