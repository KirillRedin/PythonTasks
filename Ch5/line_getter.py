"""
Program: line_getter.py
Author: Kirill Redin
Description:
    This program returns required line from file.
Inputs:
    filename (string)
    number of line (integer number)
Outputs:
    line (string)
"""

def main():
    file = get_file()
    lines = file.readlines()
    file.close()
    length = len(lines)
    
    while True:
        line_num = int(input("Enter line number between 1 and {}: ".format(length)))
        if 0 < line_num <= length:
            print(lines[line_num -1])
        else:
            break
        
def get_file():
    filename = input("Enter file name: ")
    return open(filename, 'r')

if __name__ == '__main__':
    main()
