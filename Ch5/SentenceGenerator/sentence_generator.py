"""
Program: sentence_generator.py
Author: Kirill Redin
Description:
	This program generates sentencens using simplified
	grammar.
"""
import random


PREPOSITION_PROBABILITY = 0.5
SECOND_CLAUSE_PROBABILITY = 0.2
ADJECTIVE_PROBABILITY = 0.5

def main():
	while True:
		sentence_num = int(input("Enter number of sentencens: "))
		for i in range(0, sentence_num):
			print(generate_sentence())
		print()

def generate_sentence():
	main_part = generate_noun_phrase() + ' ' + generate_verb_phrase()
	optional_part = get_word('conjunction') + ' ' + generate_noun_phrase() + ' ' + generate_verb_phrase()
	return choose_random_phrase(main_part, main_part + ' ' + optional_part, SECOND_CLAUSE_PROBABILITY)

def generate_noun_phrase():
	main_part = get_word('article') + ' ' + get_word('noun')
	optional_part = get_word('article') + ' ' + get_word('adjective') + ' ' + get_word('noun')
	return choose_random_phrase(main_part, optional_part, ADJECTIVE_PROBABILITY)

def generate_verb_phrase():
	main_part = get_word('verb') + ' ' + generate_noun_phrase()
	optional_part = generate_prepositional_phrase()
	return choose_random_phrase(main_part, main_part + ' ' + optional_part, PREPOSITION_PROBABILITY)

def generate_prepositional_phrase():
	return get_word('preposition') + ' ' + generate_noun_phrase()

def choose_random_phrase(first_phrase, second_phrase, probability):
	if random.randint(1, 1/probability) == 1:
		return second_phrase
	else:
		return first_phrase

def get_word(word_type):
	filename = word_type + 's.txt'
	file = open(filename, 'r')
	words = file.read().strip().split(',')
	return random.choice(words)

if __name__ == '__main__':
	main()