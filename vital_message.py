#!/usr/bin/env python3

"""
Title: Pirate Dogfight
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 1
Date: 15 October 2022
Source: Source: https://drive.google.com/file/d/0Bxv0SsvibDMTVUExUjFhTURCSU0/view

This game can be found on page 6 of Computer Battle Games, and it a python3 translation.

The game generates a random collection of letters that is based on the difficulty the player
selects at the beginning. The letters are then displayed on the screen for a period of time
determined by the difficulty that the player has selected. The player then needs to remember the
letters and repeat them when asks. The game is won is the letters are remember, lost if not.
"""

import util
from random import randint
import time

#Function that asks the player for the difficulty of the game
def get_difficulty():

	#Sets the correct flag
	correct = False
	difficulty = 0

	#Loops while the response is incorrect (not a number between 4 and 10)
	while not correct:
		difficulty = input("How difficult? (4-10)? ")

		#Error handling in case the player enters a letter
		try:
			difficulty = int(difficulty)

			#Is the number out of range
			if difficulty>3 and difficulty<11:
				correct = True
			else:
				print("Please enter a number between 4 to 10")
		except:
			print("Please enter a number")

	return difficulty

#Generates the phrase that the player is supposed to remember
def get_phrase(difficulty):

	phrase = ""
	alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	#Generates a phrase consisting of a number of random letters from the
	#Alphabet equal to the difficulty level
	for x in range(difficulty):
		number = randint(0,25)
		phrase += alphabet[number]

	return phrase


#Displays the instructions for the game
def instructions():

	util.clear_screen()
	print("Vital Message")
	print("===== =======")
	print("You are a laser communications operator. Your job is to intercept robot messages and relay")
	print("them to Command HQ. A vital code message is expected. If you relay it correctly, the Robot")
	print("attack will be crushed. This game tests your skill at remembering a group of letters which you")
	print("see for only a very short time. The computer will ask you for a difficulty from 4 to 10.")
	print("When you have typed in your answer, letters will appear top left of your screen and disappear")
	print("again fairly quickly. Memorize them and then type them into the computer and see if you were right.")
	print()
	input("Press enter to continue")

#Sets the game up
def start_game():

	#Clears the screen and asks whether to display the instructions
	util.clear_screen()
	print("Vital Message")

	if (util.ask_instructions() == True):
		instructions()

	#Sets the main game loop
	replay = True

	while replay:

		difficult = get_difficulty()
		main_game(difficult)

		replay = util.play_again(replay)

#Displays the phrase for a period determined by the difficulty
def display_phrase(phrase,difficulty):

	util.clear_screen()
	print("Send this message: {}".format(phrase))
	time.sleep(15-difficulty)
	util.clear_screen()

#Main Game function
def main_game(difficulty):

	#generates the phrase and displays it on the screen
	phrase = get_phrase(difficulty)
	display_phrase(phrase,difficulty)

	#Asks the player to repeat the phrase
	response = input("Enter the message: ").upper()

	#Checks if the phrase was correct
	if (response == phrase):
		print("Message Correct")
		print("The war is over")
	else:
		print("You got it wrong")
		print("You should have sent {}".input(phrase))

if __name__ == '__main__':
	start_game()