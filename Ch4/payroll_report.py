"""
Program: payroll_report.py
Author: Kirill Redin
Description:
	This program prints formatted report of the wages paid to 
	the employees.
Input:
	filename (string)
Output:
	formatted report
"""

filename = input("Enter file name: ")
file = open(filename, 'r')

print("{:^11}{:^13}{:^14}".format('Last name', 'Hourly wage', 'Hours worked'))

for line in file:
	line = line.split()
	print("{:^11}{:^13}{:^14}".format(line[0], line[1], line[2]))

file.close()
