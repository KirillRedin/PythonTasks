"""
Program: bounce_distance_counter.py
Author: Kirill Redin
Description:
	This program counts the distance traveled by the dropped ball.
Input:
	bounciness (float number)
	height (float number)
	numberOfBounces (integer number)
Calculations:
	path = 0
	for every bounce:
		bounce height = height * bounciness 
		distance = distance + height + bounce height
		height = bounce height
Output:
	distance (float number)
"""

while True:
	height = float(input("Enter ball drop height: "))
	numberOfBounces = int(input("Enter number of bounces: "))
	bounciness = float(input("Enter bounce index (0 <= index <= 1) : "))

	if(bounciness < 0 or bounciness > 1):
		print("Bounciness is incorrect", end='\n\n')
		continue

	if (numberOfBounces < 0 or height < 0):
		print("Height and number of bounces can not be negative", end='\n\n')
		continue

	distance = 0 
	for _ in range(numberOfBounces):
		bounceHeight = height * bounciness
		distance += height + bounceHeight
		height = bounceHeight
	print("Total distance is:", distance)