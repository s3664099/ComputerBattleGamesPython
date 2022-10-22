#!/usr/bin/env python3

"""
Title: Shootout
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 1.0
Date: 22 October 2022
Source: Source: https://drive.google.com/file/d/0Bxv0SsvibDMTVUExUjFhTURCSU0/view

This game can be found on page 8 of Computer Battle Games.

Basically it is a game of timing, and you have to shoot (by pressing enter) before your
opponent shoots you, but after your opponent draws.

This has been a conversion from basic into python, and fortunately the delayed input does work
reasonably well with this one since only a single key press (enter) is required.

Like the other games I have converted, I have also included instructions, plus the expansions
that they suggest.
"""

import util
from random import randint
import time

#Displays the instructions
def instructions():

	print("Shootout!")
	print("=========")
	print()
	print("You are standing back to back. You take 10 paces turn")
	print("and reach for your gun. How quick are you? Can you")
	print("shoot first?")
	print("Your computer prints out the numbers 1 to 10 to represent")
	print("the 10 paces, pauses, and then prints HE DRAWS ...")
	print("You must be ready to press enter the instant these words")
	print("come on the screen. If you are quick enough, you will win")
	print("Don't press a key before you see HE DRAWS or you will")
	print("automatically lose")
	print()
	input("Press Enter to play")

#The main game loop
def main_game():

	util.clear_screen()
	print("Cowboy Shootout")
	print("You are back to back. Take 10 paces")

	#Simulates walking 10 paces.
	for x in range(10):
		print("{} ..".format(x))
		time.sleep(1)

	#Generates a random delay of between two to five seconds
	#And calls an input with time out incase the player shoots too soon
	delay = randint(2,5)
	if (util.input_with_timeout_02("",delay)):
		print("You shot too soon.")
		print("You lose")
		return
	
	print("He draws ...")

	#Creates a loop incase the player and the opponent both miss
	while True:

		#Creates a shorter delay between when the opponent draws and shoots
		delay = randint(1,3)
		if(util.input_with_timeout_02("",delay)):

			#Player's turn for shooting
			print("But you shoot first")
			if (randint(0,10)>3):
				print("You killed him")
				return
			else:
				print("You missed")

		#Opponent's turn for shooting
		print("And he shoots")
		if (randint(0,10)>3):
			print("You are dead")
			return
		else:
			print("And he misses")

#Function for setting the game up
def start_game():

	answer,replay = util.start_game("Shoot Out")

	#If yes calls the instructions function
	if answer == True:
		instructions()

	util.clear_screen()

	while replay:
		main_game()
		replay = util.play_again(replay)

if __name__ == '__main__':
	start_game()