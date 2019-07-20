"""
Program: investment_report.py
Author: Kirill Redin
Description: This program computes an investment report.
1. Inputs:
    initial amount to be invested (floating number)
    a period of years (integer)
    an interest rate (percentage as integer)
2. Computations and outputs:
    for each year:
        interest = balance * interest rate / 100
        ending balance =  balance + interest
        print formatted result
"""

balance = float(input("Enter initial amount to be invested "))
numberOfYears = int(input("Enter a period of years "))
interestRate = int(input("Enter interest rate in percents "))
totalInterest = 0

print("Year  Starting balance  Interest  Ending Balance")

for year in range(1, numberOfYears + 1):
    interest = balance * interestRate / 100
    endingBalance = balance + interest
    print("%4d %17.2f %9.2f %15.2f" % (year, balance, interest, endingBalance))
    balance = endingBalance
    totalInterest += interest

print("Ending balance: $%.2f" % balance)
print("Total interest earned: $%.2f" % totalInterest)
    
