"""
Program: lucky_sevens.py
Author: Kirill Redin
Description:
	This program the Lucky Sevens game. Player must roll two dices. 
	If sum of dots on dices is 7, player wins $4,otherwise player
	loses $1.
Inputs:
	balance (integer number)
Computations and outputs:
	Generate two random numbers from 1 to 6. If sum on numbers
	equals 7, add 4 to player's money, otherwise subtract 1.
	Print result of the game and player balance.
	Print number of rolls it took to break the player and maximum 
	balance.
"""
import random


try:
	balance = int(input("Enter your balance: ")) 
except ValueError:
	exit()

maxBalance = balance
numberOfRolls = 0

while balance > 0:
	input("Press Enter to roll dice")
	numberOfRolls += 1

	number1 = random.randint(1, 6)
	number2 = random.randint(1, 6)

	if(number1 + number2 == 7):
		balance += 4
		result = 'WIN'
		if balance > maxBalance:
			maxBalance = balance
	else:
		balance -= 1
		result = 'LOSE'
	print('Dice 1: %d, Dice 2: %d. Result: %d - %s, Balance: %d' % (number1, number2, number1 + number2, result, balance), end='\n\n')
print('Number of rolls: %d, Max balance: %d' % (numberOfRolls, maxBalance))

