import random

print('.......................................')
print('        GUESS THE NUMBER GAME')
print('.......................................')
print()

the_number = random.randint(0,100)
guess = -1

name = input('player what is your name?  ')

while guess != the_number :
	guess_text = input('{}, guess a number between 0 and 100 :  ' .format(name))
	guess = int(guess_text)

	if guess > the_number :
		print('Sorry {},your guess of {} was too HIGH' .format(name,guess))
	elif guess < the_number :
		print('Sorry {},your guess of {} was too LOW' .format(name,guess))
	else :
		print('Excellent work {}, you won, it was {}' .format(name,guess))

print("done")