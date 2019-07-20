"""
Program: weekly_pay_calc.py
Author: Kirill Redin
Last modified: 10.11.2018
This program calculates employee's total weekly pay

Pseudocode:
hourly wage = Input hourly wage
regular hours = Input regular hours
overtiem hours = Input overtime hours
total pay = regular hours * hourly wage  + overtime hours * hourly wage * 1.5
print total pay
"""

hourly_wage = float(input("Enter hourly wage: "))
regular_hours = float(input("Enter regular hours: "))
overtime_hours = float(input("Enter overtime hours: "))
total_pay = hourly_wage * (regular_hours + overtime_hours * 1.5)
print("Employee's total wekly pay is:", total_pay)
