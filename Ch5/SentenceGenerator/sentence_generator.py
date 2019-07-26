"""
Program: sentence_generator.py
Author: Kirill Redin
Description:
	This program generates sentencens using simplified
	grammar.
"""
import random


PREPOSITION_PROBABILITY = 0.5

def main():
	while True:
		sentence_num = int(input("Enter number of sentencens: "))
		for i in range(0, sentence_num):
			print(generate_sentence())
		print()

def generate_sentence():
	return generate_noun_phrase() + ' ' + generate_verb_phrase()

def generate_noun_phrase():
	return get_word('article') + ' ' + get_word('noun')

def generate_verb_phrase():
	main_part = get_word('verb') + ' ' + generate_noun_phrase()
	optional_part = generate_prepositional_phrase()

	if random.randint(1, 1/PREPOSITION_PROBABILITY) == 1:
		return main_part + ' ' + optional_part
	else:
		return main_part

def generate_prepositional_phrase():
	return get_word('preposition') + ' ' + generate_noun_phrase()

def get_word(word_type):
	filename = word_type + 's.txt'
	file = open(filename, 'r')
	words = file.read().strip().split(',')
	return random.choice(words)

if __name__ == '__main__':
	main()