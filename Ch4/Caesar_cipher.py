"""
Program: Caesar_cipher.py
Author: Kirill Redin
Description:
	This program inputs line of plaintext and a distance 
	value then encrypts text using Caesar cipher.
Input:
	text (string)
	distance (integer number)
Computations and outputs:
	for each symbol:
		get ASCII value of the symbol
		add distance to ASCII value
		add symbol of new ASCII value to encrypted string
	return encrypted text
"""

option = input("Choose input option. 'C' - console, 'F' - file: ")
if option == 'C':
	text = input("Enter text to encrypt: ")
elif option == 'F':
	filename = input('Enter filename: ' )
	file = open(filename, 'r')
	text = file.read()
	file.close()
else:
	print('Wrong option')
	exit()

distance = int(input("Enter shift distance: "))
encryptedText = ''

for char in text:
	if ord(char) < ord('!') or ord(char) > ord('~'):
		encryptedText += char
		continue
		
	distanceToEnd = ord('~') - ord(char)
	if distanceToEnd < distance:
		distanceFromStart = distance - distanceToEnd
		coded_char = chr(ord('!') + distanceFromStart - 1)
	else:
		coded_char = chr(ord(char) + distance)
	encryptedText += coded_char

print("Encrypted result: ", encryptedText)