"""
Program: numberlines.py
Author: Kirill Redin
Description:
	This program copies file text in a new file whith added line numbers.
Input:
	file name (string)
Output:
	new file
"""

filename = input("Enter file name: ")
input_file = open(filename, 'r')
output_file = open('numbered_' + filename, 'w')
data = ''
line_num = 1

for line in input_file:
	data += '{:<4}{}'.format(line_num, line)
	line_num += 1

output_file.write(data)
output_file.close()
input_file.close()
