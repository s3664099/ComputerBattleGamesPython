#!/usr/bin/env python3

import util
from random import randint

"""
Title: Escape
Author: Daniel Isaaman & Jenny Tyler
Translater: David Sarkies 
Version: 1
Date: 27/1/2021
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTVUExUjFhTURCSU0/view

This game can be found on page 18 of Computer Battle Games, and once again is a
python translation (if I can use that word) from Basic. Like Secret Weapon, this
game could easily be transferred into C++ and Java, since it doesn't use the GET/INKEY
command.

The rules are that there is a random frequency that you must guess. You get five shots
but the catch is that if you get too high, or two low, then you die. There are actually
three robots, and you need to guess the frequency of each one of them to win the game.

I have removed the hard coded numbers so that the difficulty can be easily changed. To make
it harder, you can lower the guess_range, danger_range, and/or number_of_shots, or you can
increase the frequency range.

I have changed the text somewhat as well, because I can.

Another addition could be a difficulty setting, which changes the variables that
can set the difficulty. I haven't added one due to the number of variables that define
the difficulty of the game.
"""

#Sets the game's difficulty
guess_range = 5
danger_range = 40
frequency_range = 100
number_of_shots = 5
number_warnings = 2

#Returns an integer input.
def get_input():

	while True:
		guess = input("Guess: ")

		#Checks to see if the entry is an integer
		try:
			return int(guess)
		except:
			print("Please enter an integer")

def check_guess(frequency, guess):

	#Checks to see if the range is close enough
	#or in the danger zone (too high, or too low)
	if abs(frequency-guess)<guess_range:
		return 1
	elif frequency-guess > danger_range:
		return 2
	elif guess-frequency > danger_range:
		return 3
	else:
		return 0

#The main game loop
def game_loop(frequency):

	#Sets the number of tries for the danger zone
	low_frequency = 1
	high_frequency = 1

	for x in range(number_of_shots):

		#Get's the player's input and checks the result
		guess = get_input()
		result = check_guess(frequency, guess)

		#Takes the result and displays the appropriate message
		if result == 1:
			return ("You've done it, you've shut down the robot"), False
		elif result == 2:

			#Player death from too low a frequency
			#Sends a flag saying the player has died
			if low_frequency == number_warnings:
				return ("Too low - the building collapses"), True

			#Advises player the frequency is too low, and bad things
			#Will happen if it is too low agaon
			print("Too low, be careful, the building is shuddering")
			low_frequency += 1

		elif result == 3:

			#Player death for too high frequency and sends
			#flag that it was too high
			if high_frequency == number_warnings:
				return ("Too high, your head explodes"), True

			#Advises the player that the frequency is too high and
			#Bad things will happen if too high again
			print("Too high, be careful, your head is starting to hurt")
			high_frequency += 1

		else:

			#Nothing happens
			print("No discernable effect")

	#Time has run out and sends flag saying player has died
	return("You took too long. The robots have tortured you to death, the frequency was {}".format(frequency)), True

#Asks if the player wants instructions
def ask_instructions():

	#Asks player if they would like instructions
	answer = False

	print("Would you like instructions (Y/N) ?")
		
	#Calls the yes or no function
	answer = util.yes_or_no(answer)

	#If yes calls the instructions function
	if answer == True:
		instructions()

#Displays the instructions
def instructions():

	util.clear_screen()
	print("Escape!")
	print("=======")
	print("The Robots have caught you, taken your weapons and locked you up. Suddenly") 
	print("you remember you still have your sonar wristwatch, which can be tuned to ")
	print("produce sounds of any frequency. If you can only find the resonant frequency")
	print("of your Robot guards, they should vibrate so much they fall apart. You must")
	print("be careful not to use frequencies that are too low or the building will")
	print("vibrate and collapse on top of you. Ifyou go too high, you will get such")
	print("a terrible headache you will have to give up. Can you escape the horrors")
	print("ofthe Robot prison? (Look carefully at the program for a clue to the range")
	print("of frequencies to try.)")
	print("")
	input("Press Enter to Continue")

#Main game function
def main():

	util.clear_screen()
	print("Escape!")
	print("There are three robots to take out. Guess their frequencies")
	ask_instructions()

	replay = True

	while replay:
		#Sets the robot number and default end message
		robot = 0
		end_message = "You have shut down all three robots. You can escape"

		#Loops through the robots
		while robot < 3:

			#Sets the frequency and calls the main game loop
			print("Robot number {}".format(robot+1))
			frequency = randint(1,frequency_range)
			print(frequency)
			result, death = game_loop(frequency)

			#Checks to see if the player has died
			if death == True:
				end_message = result
				robot = 5
			else:

				#If not moves to the next robot
				print(result)
				robot +=1

		print(end_message)

		replay = util.play_again(replay)

if __name__ == '__main__':
	main()
	