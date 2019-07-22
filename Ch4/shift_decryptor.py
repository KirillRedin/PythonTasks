"""
Program: shift_decryptor.py
Author: Kirill Redin
Description:
	This program decrypts message by circular shifting a bit string 
	right, then converting it to a integer, subtracting 1 and returning
	character of resulting ASCII value.
Input:
	encrypted text (string)
Output:
	plaintext (string)
"""

def circular_shift_right(number, shift):
	new_bit_string = bit_string[-shift:] + bit_string[:-shift]
	return new_bit_string
	
encrypted_message = input("Enter message to decrypt: ")
plaintext = ""

for bit_string in encrypted_message.split():
	char_number = int(circular_shift_right(bit_string, 1), 2)
	decrypted_char = chr(char_number - 1)
	plaintext += decrypted_char
	
print("Decrypted message: ", plaintext)