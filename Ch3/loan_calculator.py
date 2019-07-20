"""
Program: loan_calculator.py
Author: Kirill Redin
Descriptiom: 
	This program calculates loan payment and prints formatted result for each month
Significant constants:
	down payments rate
	annual interest rate
	monthly payments percentage
Inputs:
	purchase price (integer number)
Computations and outputs:
	down payments = purchase price * down payments rate
	balance = purchase price - down payments
	interest = purchase price * annual interest rate
	month interest owed = interest / 12
	month principal owed = purchase price * monthly payments percentage
	month payment = month interest owed + month principal owed

	month number = 0
	while balance > 0:
		month number = month number + 1
		start balance = balance
		balance = balance - monthl principal owed
		print formatted result of current month
"""

DOWN_PAYMENTS_RATE = 0.1
ANNUAL_INTEREST_RATE = 0.12
MONTHLY_PAYMENTS_PERCENTAGE = 0.05

try:
	purchasePrice = int(input("Enter purchase price: "))
except ValueError:
	exit()

downPayments = purchasePrice * DOWN_PAYMENTS_RATE
balance = purchasePrice - downPayments
monthPrincipalOwed = purchasePrice * MONTHLY_PAYMENTS_PERCENTAGE
interest = purchasePrice * ANNUAL_INTEREST_RATE
montInterestOwed = interest / 12
monthPayment = monthPrincipalOwed + montInterestOwed
monthNumber = 0

print('%-6s%19s%20s%21s%14s%18s' % ('Month', 'Curr balance owed', 'Month interest owed', 'Month principal owed', 'Month payment', 'Rem balance'))

while balance > 0:
	monthNumber += 1
	startBalance = balance
	balance -= monthPrincipalOwed
	print('%-6d%19.3f%20.3f%21.3f%14.3f%18.3f' % (monthNumber, startBalance, montInterestOwed, monthPrincipalOwed, monthPayment, balance))

