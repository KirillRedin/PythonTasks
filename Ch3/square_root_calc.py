"""
Program: square_root_calc.py
Author: Kirill Redin
Last date modified: 15.07.2019
Description:
	This program calculates approximate square root of a number
Input:
	number (floating number)
	precision (integer number)
Calculations and output:
	1. squareRoot = 1
	2. if squareRoot ^ 2 equals number with given precision, skip step 3
	3. squareRoot = (squareRoot + number / squareRoot) / 2, go to step 2
	4. show approximate square root
"""
import math


def  sqrt(number, tolerance):
	root = 1
	while (abs(number - root ** 2) > tolerance):
		root = (root + number / root) / 2
	return root

while True:
	try :
		number = float(input("Enter a number to calculate square root: "))
		precision = int(input("Enter precision: "))
	except ValueError:
		break

	tolerance = 0.1 ** precision
	root = sqrt(number, tolerance)
	
	print('Approximate square root of %f = %.*f' % (number, precision, root), end='\n\n')
	print('Python\'s square root of %f = %.*f' % (number, precision, math.sqrt(number)), end='\n\n')