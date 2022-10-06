#!/usr/bin/env python3

import random
import string
import util
from random import randint
from time import sleep

"""
Title: Robot Invaders
Author: Daniel Isaaman & Jenny Tyler
Translater: David Sarkies 
Version: 1
Date: 26/1/2021
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTVUExUjFhTURCSU0/view

This game, Robot Invaders, appears page 14 of Computer Battlegames
The idea is that a character appears somewhere on the screen and
the player needs to replicate that character by pressing the correct key.

The game requires the util.py file to run as this contains functions that will
perform tasks across multiple games.

The inputimeout module will need to be installed (https://pypi.org/project/inputimeout/)

The program is designed to run as an executable, though the clear screen function is designed
for a unix based operating system. To have it work on a windows based system:
https://pypi.org/project/inputimeout/

Like all of the games in the above book, this one was original written in basic.
"""

#Function for player to select the difficulty of the game
def get_difficulty():

	correct_answer = False
	speed = 0

	#Checks that the input is a valid input - either 1,2, or 3
	while not correct_answer:
		print("\n\nEnter your difficulty level")
		print("1) Easy")
		print("2) Medium")
		print("3) Hard")
		print("4) Instructions")
		difficulty = input()

		if difficulty == '1' or difficulty == '2' or difficulty == '3':
			correct_answer = True
		elif difficulty == '4':
			instructions()
		else:
			print("Please enter 1, 2, or 3")

	#Sets the difficulty of the game, namely how long
	#before the input times out
	if difficulty == '1':
		speed = 15
	elif difficulty == '2':
		speed = 10
	else:
		speed = 5

	return speed

#Displays the instructions for the game
def instructions():
	util.clear_screen()
	print("Robot Invaders")
	print("----- --------")
	print()
	print("You must act quickly. Robot invaders of all kinds are approaching. You")
	print("have plenty ofweapons, but for each type of Robot you must select exactly")
	print("the right one for it to have any effect. Code symbols for each Robot will flash up on your")
	print("screen. Quickly press the key with that symbol on it - beware, some need the")
	print("shift key too - and see how many Robot invaders you can destroy.")
	print()
	input("Press enter to play")
	util.clear_screen()

#Sets up the screen
def set_screen():

	#Selects the position of the character, and the character to appear
	width = randint(0,20)
	height = randint(0,15)
	letter = random.choice(string.printable)
	screen_width = " "

	#Prints the character on the screen at the desired location
	for x in range(width):
		screen_width = screen_width + " "
	for x in range (height):
		print()
	print(screen_width+letter)

	return letter

#Sets up the score for successfully completing the level
#Certain characters attract more points than others
def set_points(letter):

	score = 10
	if letter == 'U' or letter == 'V' or letter == 'W' or letter == 'X' or letter == 'Y':
		score = 100
	return score

#The main program loop
def main():

	#Sets boolean to determine whether player wishes to play again
	replay = True

	#Clears the screen and asks for difficulty
	util.clear_screen()
	print("Robot Invaders")
	speed = get_difficulty()
	score = 0
	print("Score: "+str(score))

	while replay:

		#The game loops 25 times.
		for x in range(2):

			#The game will sleep before showing the letter
			sleep(randint(2,5))
			util.clear_screen()
			letter = set_screen()
			points = set_points(letter)
	
			#Gets the player's input
			correct = util.input_with_timeout("",speed)

			#Checks to see if the player's input is correct
			if (correct == letter):
				print("Correct")
				score += points
			else:
				print("incorrect")
			print("Score: "+str(score))

			sleep(randint(2,5))

		replay = util.play_again(replay)

if __name__ == '__main__':
	main()

