"""
Program: teacher_salary_calc.py
Author: Kirill Redin
Description:
	This program calculates teacher's salary and shows salary schedule in
	tabular format.
Inputs:
	starting salary (integer number) 
	percentage increase (integer number)
	number of the years (integer number)
Computations and outputs:
	for each year in number of years:
		print formatted row of result of that year
		next year increase = current salary * percentage increase / 100
		next year salary = current salary + next year increase		
"""
while True:
	try:
		salary = int(input("Enter starting salary: "))
		increasePercentage = int(input("Enter increase percentage: "))
		years = int(input("Enter number of years: "))
	except ValueError:
		break

	print("%5s%9s%13s" % ('Year', 'Increase', 'Salary'))

	increase = 0
	for year in range(1, years + 1):
		print('%-5d%9.3f%13.3f' % (year, increase, salary))
		increase = salary * increasePercentage / 100
		salary += increase
	print('\n')
