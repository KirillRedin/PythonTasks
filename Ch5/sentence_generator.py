"""
Program: sentence_generator.py
Author: Kirill Redin
Description:
	This program generates sentencens using simplified
	grammar.
"""

def main():
	while True:
		sentence_num = int(input("Enter number of sentencens: "))
		for i in range(0, sentence_num):
			pass
			# print(generate_sentence())
			# print(get_words('noun'))
		print()

# def generate_sentence(sentence_num):
# 	pass

# def generate_noun_phrase():
# 	pass

# def generate_verb_phrase():
# 	pass

# def generate_prepositional_phrase():
# 	pass

def get_words(word_type):
	filename = word_type + 's.txt'
	file = open(filename, 'r')
	words = file.readlines().split('\n')
	return words

if __name__ == '__main__':
	main()