#!/usr/bin/env python3

import util
import math
from random import randint

"""
Title: Secret Weapon
Author: Daniel Isaaman & Jenny Tyler
Translater: David Sarkies 
Version: 1
Date: 27/1/2021
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTVUExUjFhTURCSU0/view

This is a straight forward guessing game, which appears on page 17 of Computer Battlegames
where you select a difficulty and the numbers that you need to guess are based on 
that difficulty. This game could easily be written in Java/C++ as well, however at 
this stage I'll just stick with using python (since I might include a game selection once 
I have done all of them)

When the player makes a guess, the program will tell the player whether they are close,
miss, or hit. If the player misses too many times the player loses. If the player hits,
then the player completes the game. There is a scoring system, however the catch is that
you want to get close more often than not, as you get a score for being close.

No extra installations are required for this game, though the util file is
required for the clear screen function (which only works on Linux since I don't
use windows.)

The original game was written in basic.

I have added error handling routines to make sure that the player enters integers
"""

#Function to select the difficulty of the game
def get_difficulty():

	#Even though this is discouraged, this keeps the loop
	#going until a correct value is entered
	while True:

		print("\nEnter Difficulty")
		difficulty = input(">> ")

		#Checks to see whether the entry is an integer greater than 3
		try:
			if int(difficulty)>3:
				return int(difficulty)
			print("Please enter a difficulty greater than 3")
		except:
			print("Please enter an integer")

#Function that gets the players move. This works similar to the above
#function, except that it takes the detail of the move required
def get_move(statement):

	while True:
		try:
			player_try = input(statement)
			player_try = int(player_try)

			return player_try

		except:
			print("Please enter integers")

#The main game loop
def main_loop(difficulty, x_coord, y_coord):

	score = 0

	#Game continues for a period based on the difficulty.
	#The harder the difficulty, the longer the game
	for x in range(difficulty+5):
	
		#Gets the players moves
		x_try = get_move("Select X coordinate: ")
		y_try = get_move("Select Y coordinate: ")

		#Calculates the distance the player's shot is from the target
		hit = math.sqrt(((x_coord-x_try)**2)+((y_coord-y_try)**2))

		#Determines the hit (or closeness to it)
		if hit == 0:
			score += 10
			return "Destroyed It", score
		elif hit <= 3:
			score += 1
			print("Close")
		else:
			print("Miss")

	#Player has lost the game
	return "The Robots have seen you - AGGGHHHH ....", score

#Main game function
def main():

	util.clear_screen()
	print("Secret Weapon")

	#gets the difficulty and determines the target's position
	difficulty = get_difficulty()
	x_coord = randint(0,difficulty+1)
	y_coord = randint(0,difficulty+1)

	#Calls the main game loop, and gets the results
	result, score = main_loop(difficulty,x_coord,y_coord)

	print(result)
	print("Your score is: {}".format(score))

if __name__ == '__main__':
	main()


