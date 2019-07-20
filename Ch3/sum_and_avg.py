"""
Project: sum_and_avg.py
Author: Kirill Redin
Description: 
	This porgram allows user to input numbers and the calculates sum and average value
Inputs and computations:
	sum = 0
	while input continues:
		input new number
		sum = sum + new number
	avg = sum / numbers amount
	print result
Output: 
	sum of numbers (integer number)
	average (integer number)
"""

numbers = []

while True:
	try:
		numbers.append(int(input('Enter a number: ')))
	except ValueError:
		break

totalSum = sum(numbers)
avg = totalSum / len(numbers)
print("Sum = %d, Avg = %d" % (totalSum, avg))
