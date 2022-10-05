import random
import keyboard
import time
from os import system

#This program needs to be run as a root user

#Clears the screen
def clear():
	_ = system('clear')

def main():

	clear()
	print("Traitor's Castle")
	score = 0

	#Main Game Loop - you get ten shots
	for x in range(10):

		#Selects the position of the guard
		#Where he pops up over the wall
		r = ""
		t = random.randint(1,9)

		#Prints the screen, where 0 is the location of the guard
		#and '.' is an empty space
		for y in range (1,9):

			if (y==t):
				r=r+"0"
			else:
				r=r+"."
		print(r)

		#Gets the player input
		hit = getInput(t)

		#Determines whether hit or missed
		if (hit == True):
			print("Good Shot!")
			score+=1
		else:
			print("Missed")

	#Displays final score
	print("You hit {} out of 10".format(score))

#Function to get player input
def getInput(t):

	#Sets the time at five seconds
	time_end = time.time() + 5;

	#Loops through the time
	while time.time() < time_end:

		#Checks to see the key has been pressed
		#That represents the position of the guard
		if keyboard.is_pressed(str(t)):

			#Returns true if it is the same
			#Indicating player has hit.
			return True

	return False

if __name__ == "__main__":
	main()

			



