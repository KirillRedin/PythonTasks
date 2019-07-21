"""
Program: decimalToOctal.py
Author: Kirill Redin
Description:
	This program converts decimal numbers to octal.
Input: 
	decimal number (string)
Computations:
	Divide number by 2 until quotinent = 0. On each step add remainder
	to the left part of octal number string.
Output: 
	octal number (string)
"""

try:
	decimalNumber = int(input("Enter decimal number: "))
except ValueError:
	print("It's not a decimal number")

octalNumber = ''
quotinent = decimalNumber

while quotinent > 0:
	octalNumber = str(quotinent % 8) + octalNumber
	quotinent //= 8
		
	
print("Octal number of {} is {}".format(decimalNumber, octalNumber))