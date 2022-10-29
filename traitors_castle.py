#!/usr/bin/env python3

import util
from random import randint
import time

"""
Title: Battle at Traitor's Castle
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 1
Date: 29 October 2022
Source: Source: https://drive.google.com/file/d/0Bxv0SsvibDMTVUExUjFhTURCSU0/view

This game can be found on page 12 of Computer Battle Games, and it a python3 translation.

In this game a wall is constructed and an archer will appear at a spot along the wall. There
are 10 spots (corresponding from 0-9) and the player needs to press the correct number to hit
the archer. If the wrong number is pressed, or the player is too long in pressing the number
(five seconds) then the player will miss. 

A special archer will appear 10% of the time. If that archer is hit, the score will increase by
5, whereas a normal archer is only worth 1 point.

"""

#Displays the instructions for the game
def instructions():

	print("Battle at Traitor's Castle")
	print("==========================")
	print()
	print("The King is waging a fierce and bloody battle against his deadliest")
	print("enemy - the Traitor Baron. You are one of the King's crack bowmen and")
	print("at this very moment you are crouching behind the bushes outside the")
	print("Baron's Castle, shooting at his men as they lift their heads above")
	print("the battlements. Your computer will print a row containing eight dots")
	print("and an O. The number keys 1 to 9 correspond to the position of the 0")
	print("in the row. You have a short time to press the correct key, and hit")
	print("the O, before it disappears.")
	print("How many ofthe Baron's men can you hit?")
	print()
	input("Press enter to continue:")

#Builds the wall
def build_wall(archer,special_archer):

	#Selects a random position for the archer
	wall = ""
	archer_icon = "O"
	
	#Will this be a special archer. Changes the icon if so
	if (special_archer):
		archer_icon = "S"

	
	#Builds the wall with the archer in position
	for y in range(11):

		if archer == y:
			wall = "{}{}".format(wall,archer_icon)
		else:
			wall = "{}.".format(wall)

	return wall

#Checks whether the archer is a special archer
def check_special_archer():

	#10% chance of there being a special archer
	check_chance = randint(0,10)
	special_archer = False

	#If it is sets the special archer flag
	if check_chance == 1:
		special_archer = True

	return special_archer

#Main game function
def main_game():

	#Player's score is set at 0
	score = 0

	#The game runs for 10 turns
	for x in range(10):

		#Positions the archer
		archer = randint(0,9)
		special_archer = check_special_archer()

		#Builds and displays the wall for this turn
		util.clear_screen()
		print()
		print(build_wall(archer,special_archer))

		position = util.input_with_timeout_no_comment("", 5)
		
		try:
			if int(position) == archer:
				print("Good shot!")

				#Score is based on whether it was a special archer or not
				if special_archer:
					score +=5
				else:
					score +=1

			else:
				print("Missed")
		except:
			print("Missed")	

		time.sleep(2)

	print("You hit {} times out for 10".format(score))

#Starts the game
def start_game():

	#Displays the title and asks for instructions
	answer,replay = util.start_game("Battle at Traitor's Castle")

	if answer:
		instructions()

	#Main loop
	while replay:

		main_game()

		replay = util.play_again(replay)

if __name__ == '__main__':
	start_game()