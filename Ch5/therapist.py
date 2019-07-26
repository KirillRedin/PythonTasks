"""
Program: therapist.py
Author: Kirill Redin
Description:
	This porgram emulates psycotherapist by creating 
	simple answers on user's sentences
"""
import random


hedges = ('Tell me more about it', 'Does it disturb you',
			'And what do you think about it')
qualifiers = ('What makes you think that ', 'You seem to think that ',
				'Can you explain why ', 'What do you think a reason that ' )
replacements = {'i': 'you', "i'm": 'you are', 'am': 'are',
				'me': 'you', 'my': 'your', 'mine': 'yours', 
				'us': 'you', 'you': 'I', 'your': 'my',
				'yours': 'mine', 'are': 'am'}
HEDGE_PROBABILITY = 0.2


def main():
	display_greeting()
	while True:
		user_message = input(">> ")
		if user_message == 'exit':
			break
		therapist_message = generate_message(user_message)
		print(therapist_message)
	pass

def generate_message(user_message):
	if random.randint(1, 1 / HEDGE_PROBABILITY) == 1:
		return random.choice(hedges)
	else:
		return random.choice(qualifiers) + change_person(user_message)


def change_person(user_message):
	new_message = ''
	last_word = ''
	for word in user_message.split():
		if word == 'are' and last_word != "you":
			new_message += word + ' '
			continue
		new_message += replacements.get(word.lower(), word) + ' '
		last_word = word
	return new_message

def display_greeting():
	print("Hello! Tell me what's bothering you?")

if __name__ == '__main__':
	main()
