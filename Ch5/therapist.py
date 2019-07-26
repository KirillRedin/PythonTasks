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
previous_topic_qualifiers = ('Earlier you said that ', 'You mentioned that ')
HEDGE_PROBABILITY = 0.2
PREVIOUS_TOPIC_PROBABILITY = 0.1
MINIMUM_CHANGES = 4

def main():
	changes_made = 0 # var to control changes in history for topic shifting
	history = []
	display_greeting()
	while True:
		user_message = input(">> ")
		history.append(user_message)
		changes_made += 1
		if user_message == 'exit':
			break
		therapist_message = generate_message(user_message, history, changes_made)
		print(therapist_message)
	pass

def generate_message(user_message, history, changes_made):
	# Chance to choose hedge for answer is 1/5
	if random.randint(1, 1 / HEDGE_PROBABILITY) == 1:
		return random.choice(hedges)
	# Chanse to shift to older topic is 1/10. Must be done not less than 4 history changes.
	if random.randint(1, 1 / PREVIOUS_TOPIC_PROBABILITY) == 1 and changes_made > MINIMUM_CHANGES:
		return random.choice(previous_topic_qualifiers) + change_person(random.choice(history[:-MINIMUM_CHANGES]))
	# If none of previous options were executed, just change person of user message with standart qualifier
	return random.choice(qualifiers) + change_person(user_message)


def change_person(user_message):
	new_message = ''
	last_word = '' # If we want to change "You are" to "I am", we need to save previous word

	# I'm using split because traversing replacemets and replacing by dict's value will made double changes
	for word in user_message.split(): # Because of split by whitespace I can't change whole phrase 
		word = word.lower()
		if word == 'are' and last_word != "you": # Checking if whole phrase was "you are"
			new_message += word + ' '
			continue
		new_message += replacements.get(word, word) + ' ' # Replace word if it in a dict or left it by default
		last_word = word
	return new_message

def display_greeting():
	print("Hello! Tell me what's bothering you?")

if __name__ == '__main__':
	main()
