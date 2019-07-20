import random


smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
victoryNumber = random.randint(smaller, larger)
count = 0

while True:
	count += 1
	userNumber = int(input("Enter your guess: "))

	if(userNumber == victoryNumber):
		print('YOU WON! Number of guesses: ', count)
		break
	elif(userNumber < victoryNumber):
		print('Too small')
	else:
		print('Too large')


