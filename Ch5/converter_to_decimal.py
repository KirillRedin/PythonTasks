"""
Program: converter_to_decimal.py
Author: Kirill Redin
Description:
	This program converts number in any base to decimal.
"""

digits_dict = {'0': 0, '1': 1, '2': 2, '3': 3, 
				'4': 4, '5': 5, '6': 6, '7': 7,
				'8': 8, '9': 9, 'A': 10, 'B': 11,
				'C': 12, 'D': 13, 'E': 14, 'F': 15}

def main():
	number = input("Enter number to convert: ")
	base = int(input("Enter base of a number: "))
	decimal = rep_to_decimal(number, base)
	print("Decimal representation of {} with the base {} = {}".format(number, base, decimal))

def rep_to_decimal(number, base):
	decimal = 0
	number = number[::-1].upper() # Reverse sequence to simplify traversing and make all upper case
	for i in range(0, len(number)):
		char = number[i]
		decimal += digits_dict[char] * base ** i
	return decimal

if __name__ == '__main__':
	main()