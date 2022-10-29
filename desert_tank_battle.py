#!/usr/bin/env python3

import util
from random import randint
import math

"""
Title: Desert Tank Battle
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 1
Date: 26 October 2022
Source: Source: https://drive.google.com/file/d/0Bxv0SsvibDMTVUExUjFhTURCSU0/view

This game can be found on page 10 of Computer Battle Games, and it a python3 translation.

This game sets the position of the enemy, and the player needs to determine where the enemy is
and fire at it. The player will set an elevation for the gun, and a direction. Once fired
the computer will determine if it is a hit or a miss. If it is a miss, the computer will determine
how far off the shot is, and provide the player with a hint as to where the enemy is located

Added functionality so that the enemy can shoot back at the player.

"""

#Displays the instructions for the game
def instructions():

	print("Desert Tank Battle")
	print("==================")
	print("The last major stronghold of Robot forces outside the U.R.S* is hidden in ancient")
	print("castle ruins in the middle ofthe desert. A fleet ofdesert hovertanks has beensent")
	print("to destroy it and you are the commander. Your tank controls the five remaining")
	print("missiles.")
	print("You must assess carefully the direction and elevation before you launch each")
	print("one. Your computer will ask you for a direction angle between —90° (extreme left)")
	print("and +90° (extreme right) and an elevation angle between 0° (along the ground) and")
	print("90° (straight up in the air). The elevation determines the distance the missile will")
	print("travel.")
	print("Is your aim good enough to destroy the robot stronghold?")
	print("")
	input("Press enter to continue:")

#Asks the player a question, and returns a number between upper and lower
def get_answer(text,lower,upper):

	while True:
		response = input(text)

		try:

			#turns the answer into a number
			response = int(response)

			#Checks if the answer is within range
			if response <= upper and response >= lower:
				return response

			else:
				print("Please enter a number between {} and {}!".format(lower,upper))

		#Handles the error if the response is not a number
		except:
			print("Please enter a number")

#Takes the direction that the player fired and the position of the enemy
def get_result_direction(player_direction,direction):

		result_direction = ""

		#Compares the direction the player fired and returns the result
		if (player_direction<direction):
			result_direction = "to the left"
		elif (player_direction>direction):
			result_direction = "to the right"	

		return result_direction

#Takes the distance the player fired and the position of the enemy, as well as the directions
def get_result_distance(player_distance,distance,direction,player_direction):

		result_distance = ""

		#Has the player also been off with regards to the direction
		if (direction!=player_direction and abs(player_distance-distance)>.05):

			result_distance = " and "

		#Compares the position of the enemy and the position the player fired and returns the result
		if (distance-player_distance>.05):
			result_distance = "{}not far enough".format(result_distance)

		if (player_distance-distance>.05):
			result_distance = "{}too far".format(result_distance)

		return result_distance

#Checks if the player has been spotted
def check_spotted(spot_chance):

	#Gets a random number
	spotted = randint(0,20)
	been_spotted = False

	#Checks if the number is less than the chance
	if spotted < spot_chance:
		been_spotted = True

	return been_spotted

#Main game loop
def main_game(direction,distance):

	response = ""
	spot_chance = 1

	#The player has five goes
	for x in range (5):
		player_direction = get_answer("Direction (-90 to 90): ", -90,90)
		player_elevation = get_answer("Elevation (0 to 90): ", 0,90)

		#Converts the distance
		p_distance_1 = math.sin(2*(player_elevation/180*3.1416))

		#Did the player hit the enemy
		if (abs(direction-player_direction)<2 and abs(distance-p_distance_1)<.05):
			response="Kaboom!!\nYou did it. You hit the blighter"
			x=5
		else:
			result_direction = get_result_direction(player_direction,direction)

			result_distance = get_result_distance(p_distance_1,distance,direction,player_direction)

			print("Missile Landed {}{}".format(result_direction,result_distance))

			#Checks to see if player has been spotted
			if check_spotted(spot_chance):
				response = "You have been spotted by the enemy\nhe shoots and destroys you"
				x=5

			#Chance of being spotted increases exponentially
			spot_chance *= 2

	if response == "":
		response = "Disaster - you failed\nRetreat in disgrace"

	return response

def start_game():

	answer,replay = util.start_game("Desert Tank Battle")

	while replay:

		#Generates the location of the enemy
		direction = randint(-90,90)
		distance = randint(0,100)/100
		print(main_game(direction,distance))

		replay = util.play_again(replay)


if __name__ == '__main__':
	start_game()