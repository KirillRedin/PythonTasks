"""
Program: nautical_miles_calc.py
Author: Kirill Redin
Last modified: 10.11.2018
This program converting kilometers to nautical miles

Pseudocode:
distance in kilometers = Input distance
distance in nautical miles = distance in kilometers / 10000 * 90 * 60
print distance in nautical miles
"""

distance_in_km = float(input("Enter distance in kilometers: "))
distance_in_nmi = distance_in_km / 10000 * 90 * 60
print(distance_in_km, "kilometers =", distance_in_nmi, "nautical miles")
