"""
Program: tax_calc.py
Author: Kirill Redin
Last Modified 10.11.2018
This program computes person's tax

Pseudocode:
gross income = Input gross income
number of dependents = Input number of dependents
income tax = (gross income - 10000 - number of dependents * 3000) * 0.2
print income tax
"""

# Initialize the constants
TAX_RATE = 0.2
STANDART_DEDUCTION = 10000
ADDITIONAL_DEDUCTION = 3000

#User input
gross_income = float(input("Enter your gross income: "))
num_of_dependents = int(input("Enter your number of dependents: "))

#Calculating income tax
income_tax = (gross_income - STANDART_DEDUCTION - num_of_dependents * \
              ADDITIONAL_DEDUCTION) * TAX_RATE
print("Your income tax is:", round(income_tax, 2))
