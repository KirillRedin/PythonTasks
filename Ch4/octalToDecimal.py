"""
Program: octalToDecimal.py
Author: Kirill Redin
Description:
	This program converts octal numbers to decimal.
Input: 
	octal number (string)
Computations:
	for each digit in octal number beginning from the right:
		number = number + digit * 8 ^ postirion of digit  (begins from 0)
Output: 
	decimal number (integer)
"""

octalNumber = input("Enter octal number: ")
decimalNumber = 0
power = len(octalNumber) - 1

for digit in octalNumber:
	if digit < '0' or digit > '8':
		print("It's not an octal number")
		exit()
	decimalNumber += int(digit) * 8 ** power
	power -= 1

print("Decimal number of {} is {}".format(octalNumber, decimalNumber))