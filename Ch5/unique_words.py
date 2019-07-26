"""
Program: unique_words.py
Author: Kirill Redin
Description:
	This program outputs unique words from a file
	in alphabeticaal order.
"""

def main():
	filename = input("Enter file name: ")
	words = get_words(filename)
	unique_words = get_unique_words(words)
	print(unique_words)

def get_words(filename):
	file = open(filename, 'r')
	words = []
	for line in file:
		words += (line.split())
	return words

def get_unique_words(words):
	unique_words = {}
	for word in words:
		unique_words[word] = words.count(word)
	unique_words = list(unique_words.items())
	unique_words.sort(key=lambda x: x[0].lower())
	return unique_words

if __name__ == '__main__':
	main()