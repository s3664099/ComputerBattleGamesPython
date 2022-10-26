#!/usr/bin/env python3

import util
from random import randint
import math

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

def main_game(direction,distance):

	for x in range (5):
		player_direction = get_answer("Direction (-90 to 90): ", -90,90)
		player_elevation = get_answer("Elevation (0 to 90): ", 0,90)

		p_distance_1 = math.sin(2*(player_elevation/180*3.1416))

		if (abs(direction-player_direction)<2 and abs(distance-p_distance_1)<.05):
			print("Kaboom!!!")
			print("You did it. You hit the blighter")
			return

		result_direction = ""

		if (player_direction<direction):
			result_direction = "to the left"
		elif (player_direction>direction):
			result_direction = "to the right"

		result_distance = ""

		if (direction!=player_direction and abs(p_distance_1-distance)>.05):

			if (distance-p_distance_1>.05):
				result_distance = "and not far enough"

			if (p_distance_1-distance>.05):
				result_distance = "and too far"

		print("Missile Landed {} {}".format(result_direction,result_distance))

	print("Disaster - you failed")
	print("Retreat in disaster")

def start_game():

	answer,replay = util.start_game("Desert Tank Battle")

	while replay:
		direction = randint(-90,90)
		distance = randint(0,100)/100
		main_game(direction,distance)


if __name__ == '__main__':
	start_game()