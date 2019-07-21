"""
Program: Caesar_cipher.py
Author: Kirill Redin
Description:
	This program inputs encrypted with the Caesar cipher
	text and a distance value and outputs plaintext
Input:
	encrypted text (string)
	distance (integer number)
Computations and outputs:
	for each symbol:
		get ASCII value of the symbol
		subtract distance from ASCII value
		add symbol of new ASCII value to plaintext string
	return plaintext
"""

text = input("Enter text to decrypt: ")
distance = int(input("Enter shift distance: "))
plaintext = ''

for char in text:
	if ord(char) < ord('!') or ord(char) > ord('~'):
		plaintext += char
		continue
		
	distanceFromStart = ord(char) - ord('!')
	if distanceFromStart < distance:
		distanceToEnd = distance - distanceFromStart
		decoded_char = chr(ord('~') - distanceToEnd + 1)
	else:
		decoded_char = chr(ord(char) - distance)
	plaintext += decoded_char

print("Decrypted result: ", plaintext)