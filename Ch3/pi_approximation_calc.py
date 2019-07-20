"""
Program: pi_approximation_calc.py
Author: Kirill Redin
Description: 
	This program calculates apptoximate value of pi using Leibniz formula
Input:
	number of iterations (integer number)
Computations:
	result = 0
	for number of iterations:
		result = result + ((-1) ^ number of iteration) / (2 * number of iteration + 1)
	pi = result * 4
Output:
	approximate value of pi (float)
"""
import math


while True:
	try:
		numOfIter = int(input("Enter number of iterations: "))
	except ValueError:
		break

	if(numOfIter < 0):
		print("Number of iterations can not be negative")
		continue

	result = 0
	for i in range(0, numOfIter):
		result = result + ((-1) ** i) / (2 * i + 1)
	pi = result * 4
	print("Approximate value of pi after %d iterations is %f\nPython's value of pi is %f" % (numOfIter, pi, math.pi), end='\n\n')
