"""
Program: guessing_game_2.py
Name: Kirill Redin
Description: 
	This is a game where user thinks of a number that the computer must guess
	in minimum number of guesses.
Input data: 
	smaller (integer number) 
	larger (integer number)
	hint (string)
Calculations:
	While number is not guessed:
		number = (smaller + larger) / 2
		if number < guessed number:
			larger = number
		else:
			smaller = number
Output:
	number (integer numberr)
	numberOfGuesses (integer number)
	minNumberOfGuesses (integer number)
"""

import random
import math


smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
count = 0
minNumberOfGuesses = round(math.log(larger - smaller + 1, 2))

while True:
	count += 1
	number = int((smaller  + larger) / 2)
	userMessage = input("Is your number %d.\nIf result is correct, enter 'Yes'.\nIf result is too small, enter '<'.\
						\nIf result is too large, enter '>'.\nEnter a message: " % number)
	print('\n\n')

	if(userMessage == 'Yes'):
		print('Your number is %d.\nNumber of guesses: %d.\nMinimum number of guesses %d.' % (number, count, minNumberOfGuesses))
		break
	elif(userMessage == '<'):
		larger = number
	elif(userMessage == '>'):
		smaller = number
	else:
		print("Please, enter correct value", end='\n\n')
		count -= 1

	if (larger - smaller == 1):
		print('I think you are cheating. Try again.')
		break


