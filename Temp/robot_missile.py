import random

def main():

	playing = True

	while playing == True:

		foundLetter = main_game()

		if foundLetter == False:
			print("BOOM!!!! You blew it")
			print("The correct code was {}".format(letter))
		else:
			print("Tick.....fzzzz.....click")
			print("You did it")

		answer = input("Do you want to play again?\n")

		if answer[:1].upper() != "Y":
			playing = False


def main_game():

	foundLetter = False
	turn = 0
	number = 65
	n = random.randint(number,number+26)
	letter = chr(n)

	print("Robot Missile\n\n")
	print("Type the correct code")
	print("Letter (A-Z) to Defuse the missile")
	print("you have 4 chances\n")

	while turn < 4:

		turn +=1
		correctInput = False
	
		while correctInput == False:
			attempt = input("Enter a letter between A and Z\n")

			attempt = attempt.upper()
	
			if attempt.isalpha() and len(attempt) == 1:
				correctInput = True

			if correctInput == False:
				print("Invalid input, try again\n")

		if attempt < letter:
			print("You are too low")
		elif attempt > letter:
			print("You are too high")
		else:
			foundLetter = True
			turn = 4
	return foundLetter

if __name__ == "__main__":
	main()