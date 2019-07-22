1   """
2   Program: numberlines.py
3   Author: Kirill Redin
4   Description:
5   	This program copies file text in a new file whith added line numbers.
6   Input:
7   	file name (string)
8   Output:
9   	new file
10  """
11  
12  filename = input("Enter file name: ")
13  input_file = open(filename, 'r')
14  output_file = open('numbered_' + filename, 'w')
15  data = ''
16  line_num = 1
17  
18  for line in input_file:
19  	data += '{:<4}{}'.format(line_num, line)
20  	line_num += 1
21  
22  output_file.write(data)
23  output_file.close()
24  input_file.close()
