"""
Program: population_growth_predictor.py
Author: Kirill Redin
Description:
	This program predict how population will grow in time
Inputs:
	initial number of organisms  (integer number)
	rate of growth (integer number)
	number of hours to achieve rate of growth (integer number)
	number of hours during which the population growth (integer number)
Computations:
	every number of hours to achieve rate of growth till population growth:
		number of organisms = number of organisms * rate of growth
Outputs:
	predicted number of organisms (integer value)
"""

while True:
	try:
		numOfOrg = int(input("Enter number of organisms: "))
		rate = int(input("Enter rate of growth: "))
		rateTime = int(input("Enter number of hours to achieve rate: "))
		growthTime = int(input("Enter number of hours during which population growth: "))
	except ValueError:
		print("Wrong value")
		break

	if numOfOrg < 0 or rate < 0 or rateTime < 0 or growthTime < 0:
		print("Values can not be negative", end='\n\n')
		continue

	for _ in range(0, growthTime, rateTime):
		numOfOrg *= 2

	print("Number of organisms after %d hours will be %d" % (growthTime, numOfOrg), end='\n\n')

