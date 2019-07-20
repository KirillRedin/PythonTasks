"""
Program: light_year.py
Author: Kirill Redin
Last modified: 10.11.2018
This program calculating value of light year in meters

Pseudocode:
light year = spheed of light * 365 * 24 * 60
print light year
"""

LIGHT_SPEED = 3 * 10 ** 8
DAYS_IN_YEAR = 365
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60

light_year = LIGHT_SPEED * DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR \
             * SECONDS_IN_MINUTE

print("Light year =", light_year, "meters")
