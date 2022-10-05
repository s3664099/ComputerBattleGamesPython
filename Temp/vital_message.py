from os import system
import random
from time import sleep

#Clears the screen
def clear():
	_ = system('clear')

def main():

	#Sets the game loop
	game = True

	while game == True:
		print("The Vital Message")
		print("-----------------")
		print()
		print("How difficult? (4-10)")
	
		#Gets the difficulty, and length of message based on the difficulty
		difficulty = get_difficulty()
		message = get_message(difficulty)

		#Prints the message on the screen and then clears it
		clear()
		print("Send this message: \n")
		print(message)
		sleep(5)
		clear()

		print("Send the message")
		attempt = input()
		attempt = attempt.upper()

		#Checks to see if the message is correct
		if attempt == message:
			print("The message is correct")
			print("The war is over!!")
		else:
			print("You got it wrong")
			print("You should have sent: {}".format(message))

		print("Do you want to play again?")
		answer = input()

		if (answer.upper() == 'N'):
			game = False

#Function to generate the message
def get_message(difficulty):

	message = ""
	number = 65

	#Returns a string of letters based on the difficulty
	for x in range(difficulty):
		n = random.randint(number,number+26)
		letter = chr(n)
		message += letter
	return message;

#Gets the difficulty of the game, which determines the length of the message
def get_difficulty():

	valid = False;

	while valid == False:

		#Confirms that the difficulty is a number, and between 4 and 10
		try:
			difficulty = int(input())

			if (difficulty > 3) and (difficulty <11):
				return difficulty

			print("You must enter a value beteen 4 and 10")
		except:
			print("You must enter a number")

if __name__ == "__main__":
	clear()
	main()