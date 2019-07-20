"""
Program: year_minutes.py
Author: Kirill Redin
Last modified: 10.11.2018

This program calculates the number of munites in a year

Pseudocode:
number of minutes = 365 * 24 * 60
print number of minutes
"""

DAYS_IN_YEAR = 365
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60

year_minutes = DAYS_IN_YEAR * HOURS_IN_DAY* MINUTES_IN_HOUR
leap_year_minutes = year_minutes + HOURS_IN_DAY * MINUTES_IN_HOUR
print("There are", year_minutes, "minutes in a year and", \
      leap_year_minutes, "minutes in a leap year")
