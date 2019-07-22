"""
Program: shift_encryptor.py
Author: Kirill Redin
Description:
	This program encrypts message by adding 1 to each character's
	ASCII value, converting it to a bit string and then using
	circular left shift of a bit string.
Input:
	plaintext (string)
Output:
	encrypted message (string)
"""

def circular_shift_left(bit_string, shift):
	new_bit_string = bit_string[shift:] + bit_string[:shift]
	return new_bit_string


plaintext = input("Enter message to encrypt: ")
encrypted_message = ""

for char in plaintext:
	bit_string = bin(ord(char) + 1)[2:]
	encrypted_string = circular_shift_left(bit_string, 1)
	encrypted_message += encrypted_string + ' ' 

print("Encrypted message: ", encrypted_message)