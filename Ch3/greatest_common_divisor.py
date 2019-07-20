"""
Program: greatest_common_divisor.py
Author: Kirill Redin
Description:
	This program computes greatest common divisor of two number using Euclid's algorithm
Inputs:
	first number (integer number)
	second number (integer number)
Computations and outputs:
	while smaller number not equals to 0:
		calculate reminder of larger number / smaller number
		print formatted row of result of current iteration
		larger number = smaller number
		smaller number = remainder
	print the resulting GCD
"""

while True:
	try:
		num1 = int(input("Enter first number: "))
		num2 = int(input("Enter second number: "))
	except ValueError:
		break

	if(num1 <= 0 or num2 <= 0):
		print('Number must be positive', end='\n\n')
		continue

	smallerNum = min(num1, num2)
	largerNum = max(num1, num2)

	print("%-10s%14s%15s%9s" % ('Iteration', 'Larger number', 'Smaller number', 'Reminder'))
	count = 0
	while smallerNum != 0:
		count += 1
		reminder = largerNum % smallerNum
		print("%-10d%14d%14d%9d" % (count, largerNum, smallerNum, reminder))
		largerNum = smallerNum
		smallerNum = reminder

	print("\nGCD = %d\n\n" % largerNum)