#!/usr/bin/python3

import random
import math
from os import system

#Function to make sure the correct input is entered
#Takes the range of the integers that are acceptable
def get_input(low, high):

	#Flag to determined whether the correct input
	#has been entered
	correct_input = False

	while (correct_input == False):
		player_input = input()

		#Checks to see if the input is an integer
		try:
			player_input = int(player_input)
			correct_input = True
		except:
			a=1

		#If it is an integer, confirms that it is within range
		if (correct_input == True):

			if player_input <low or player_input > high:
				correct_input = False

		#If the input is not correct, an error message is printed
		if (correct_input==False):
			print("Please enter an integer between {} and {}".format(low,high))

	return player_input


#Function that fires the shot and determines whether there has been a hit
def fire_shot(facing, distance):
	for guess in range (5):

		#Gets the player input to determine facing and elevation
		print("\nSelect Direction (-90 to 90)")
		direction = get_input(-90,90)

		print("Select Elevation (0 to 90)")
		elevation = get_input(0,90)

		#Determines the distance that the shot has been fired
		shot_distance = math.sin(2*(elevation/180*3.1416))

		#Determines whether there as been a hit, within the margin of error
		if abs(facing-direction)<2 and abs(distance-shot_distance)<0.05:
			return True

		#The shot has missed so the player is advised
		#on the location of the shot
		else:
			print("\nThe Missile Landed")
			if (facing<direction):
				print("To the left")
			elif (facing>direction):
				print("To the right")

			#Determines whether both entries are incorrect
			if abs(distance-shot_distance)>0.05 and facing != direction:
				print("and")

			if (distance-shot_distance<0.05):
				print("Too Far")
			elif (distance-shot_distance>0.05):
				print("Not far enough")

		spotted = random.randint(0,9)

		if (spotted == 0):
			return 3

	return False

#Function to print a victory text
def hit():
	print("***KABOOOM****")
	print("You did it!!!")

#Function to print failed text
def missed():
	print("DISASTER - you failed")
	print("retreat in disgrace")

def spotted():
	print("The robot has spotted you")
	print("The fire and destroy your artillery")

#Function to set the game up
def main():

	system("clear")
	print("Desert Tank Battle")

	#Sets the location of the target
	facing = random.randint(-90,90)
	distance = random.uniform(0,1)

	#Determins the results of the players actions
	result = fire_shot(facing, distance)

	system("clear")


	#Determines whether it was a hit or miss or player was spotted
	if result == 3:
		spotted()
	elif result:
		hit()
	else:
		missed()

if __name__ == "__main__":
	main()

