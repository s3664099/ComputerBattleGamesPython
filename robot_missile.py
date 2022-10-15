#!/usr/bin/env python3

"""
Title: Robot Missile
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 0
Date: 15 October 2022
Source: Source: https://drive.google.com/file/d/0Bxv0SsvibDMTVUExUjFhTURCSU0/view

This game can be found on page 4 of Computer Battle Games, and it a python3 translation.
"""

import util
from random import randint
import time

#Holds the letters of the alphabet
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#Displays the full instructions for the game
def instructions():

	util.clear_screen()
	print("Robot Missile")
	print("===== =======")
	print("The year is 2582 and the people of Earth are in the midst of a battle against the Robots.")
	print("A lethal Robot Missile has just landed and everyone is depending on you to find the secret")
	print("code which unlocks its defuse mechanism. If you fail, the entire Earth Command Headquarters")
	print("will be blown up. Your computer knows what the code letter is. You must type in your guess and")
	print("it will tell you whether the code letter is earlier or later in the alphabet. You have four")
	print("chances to find the correct letter before the missile blows up.")
	print()

#Retrieves a random letter of the alphabet
def get_letter():

	letter = randint(0,25)
	return alphabet[letter]

#Checks the position of the player's response to the position of the
#letter in the alphabet
def check_position(response,letter):

	for x in alphabet:

		#If it hits the response before hitting the letter
		if response == x:
			print("Later")
			break

		#If it hits the letter before hitting the response
		elif letter == x:
			print("Earlier")
			break

def main_game(letter):

	#Sets the won flag
	won = False

	#The player gets four goes
	for x in range(4):

		#gets the response and sets it to upper case
		response = input("Please select a letter: ").upper()

		#The player guesses the latter		
		if (response == letter):
			print("Tick ... fzzz ... click ...")
			time.sleep(2)
			print("You did it!")

			#The win flag is set
			won = True
			break

		#The player's guess is incorrect
		else:
			check_position(response,letter)

	#The win flag indicates a loss
	if not won:
		print("BOOOOMMMMMM........")
		print("You blew it.")
		print("The correct code was {}".format(letter))

def start_game():

	util.clear_screen()
	print("Robot Missile")

	if (util.ask_instructions() == True):
		instructions()
	else:
		print()
		print("Type the correct code letter (A-Z)")
		print("to defuse the missile")
		print("you have 4 changes")

	input("Press enter to continue")

	replay = True

	while replay:

		main_game(get_letter())
		replay = util.play_again(replay)

if __name__ == '__main__':
	start_game()