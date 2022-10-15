#!/usr/bin/env python3

"""
Title: Wizard's Wall
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 1.1
Date: 8 March 2021
Updated Date: 15 October 2022
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTVUExUjFhTURCSU0/view

This is another game from the Computer Battlegames book, this one appearing
on page 26. This was quite a tricky one to translate, first because no
description of the code was included, and also the game jumps around more
often than not, and getting a feel of the flow of the game was rather tricky.

I'm not entirely sure whether I have entered it correctly, since the game also
uses a number of mathematical equations which aren't explained, so I have
simply relied on guess work, and well as constructing the functions so they
hopefully the flow works.

Also, writing it using the VIM editor means that the order isn't the best.
Beyond translating the game to Python, I haven't done much to change it. Also
I have used some hardcoded values, which need to change if we want to make
the wall larger. However, the lack of comments means that this can be quite
difficult as well.

Oh, and the use of single letter variables in the listing meant that this made
the game somewhat trickier to code as well.
"""

import util
import time
import math
from random import randint

wall_length = 8
wall_height = 8

#Sets up the wall that the player has to knock down
def set_up():

	#creates a wall that is 8 wide and 8 high
	wall = [[0 for x in range(wall_length)] for y in range(wall_height)]
	wall_detail = [0 for y in range(wall_height)]
	
	#Populates the values of the wall at 4 (though could be changed
	#since this only says whether there is a hole or not).
	for x in range(wall_length):
		for y in range(wall_height):
			wall[x][y] = 4 
	return wall, wall_detail

#Simply displays the instructions for the game
def display_instructions():
	util.clear_screen()
	print("You are attacking the last stronghold of the notorious wizard,")
	print("who is hidden behind an endless stone wall, each stone being")
	print("one of his former victims. Only you can attack and free them")
	print("from his magic.")
	print("You must destory the wall using catapults, but beware, the")
	print("wizard has the power to move the wall back and forth, and")
	print("occasionally to deflect your shots back at you")
	press_enter()
	util.clear_screen()
	print("After each shot you are shown a cross-section of the wall")
	print("showing how much damage there is")
	print("Note there are certain key stones that produce lots of damage")
	print("and also, the faster the boulder is moving horizontally, the")
	print("more damage it will cause. Can you defeat the wizard in time")
	print("to save the thousands of trapped souls ......")
	press_enter()
	util.clear_screen()

#Function to call the player to press enter to continue
def press_enter():
	input("<<press Return to continue>>")

#Function to request the player to enter the difficulty level
#Also validates the input to make sure it is an integer between 
#1 and 5.
def get_difficulty():

	correct = False

	while not correct:

		difficulty = input("Difficulty: 5 = easy, 1 = difficult: ")
		try:
			if int(difficulty) > 0 and int(difficulty) < 6:
				return difficulty
			else:
				print("\nPlease enter a difficulty between 1 and 5\n")
		except:
			print("\nPlease enter an integer between 1 and 5\n")

#function that starts the game	
def start_game():

	util.clear_screen()
	print("The Wizard's Wall")
	correct = False

	#Offers to display the instructions and gets the difficulty
	while not correct:
		response = input("Do you want instructions? ")

		if response.lower()[:1] == "y":
			display_instructions()
			correct = True
		elif response.lower()[:1] == "n":
			correct = True
		else:
			print("Please enter (Y)es or (N)o")

	replay = True

	while replay:
		#Sets up the wall and executes the main game
		difficulty = get_difficulty()
		wall, wall_detail = set_up() 
		result = main_game(difficulty,wall, wall_detail)

		#Displays the result of the game
		if result == True:
			print("You have managed to break a hole in the wizard's wall")
			print("You have beaten his magic powers, and freed his victims")
		else:
			print("You have been turned into stone")
			print("You are now a part of the wizard's wall")
			print("Too bad, so sad.")

		replay = util.play_again()

#Function that prints out the wizard's wall to show the player
#what has been knocked down, and what remains
def display_wall(wall):
	
	time.sleep(1)
	util.clear_screen()
	
	for y in range(7,0,-1):
		wall_display = ""
		for x in range (8):
			wall_display += str(wall[x][y])
		print(wall_display)

#Function that determines which way the wind is blowing
def wind():
	
	wind = randint(-20,20)
	if wind<0:
		print("Wind is blowing to the right")
	elif wind>0:
		print("Wind is blowing to the left")
	else:
		print("There is no wind")		
	return wind	

#Function that takes the player's input, namely for the elevation and the speed
#Validates the input to make sure that it is correct
def get_value(value, maximum, minimum):
	
	while True:
		val = input("give {} ({} to {}) ".format(value, maximum, minimum))
		
		try:
			if int(val) <maximum+1 and int(val)>minimum-1:
				return val
			else:
				print("Please enter a value between {} and {}".format(maximum, minimum))
		except:
			print("Please enter an integer")

#Takes the players input, and other factors, and determines the
#Result of the shot. Returns this value
def calculate(elevation, speed, distance, wind_direction, difficulty):

	elevation = int(elevation)/180*3.1416
	dw = int(distance)-int(wind_direction)
	dwexp = (5*(dw)**2) 
	elecos = (int(speed)*math.cos(elevation))**2
	height = math.tan(elevation)*dw-dwexp/elecos
	height = (height/int(difficulty))

	return height, elevation

#Main game loop
def main_game(difficulty,wall, wall_detail):

	distance = randint(21,101)
	z = 0
	turn = 0
	
	#If the wall moves three times, the player loses
	while turn < 3:
		display_wall(wall)

		#Winning Condition
		if z == 1:
			return True

		#Calculates information pertaining to the shot.
		#Provides distance information
		print("You are {} yards away".format(distance))
		wind_direction = wind()
		elevation = get_value("elevation",90,1)
		speed = get_value("speed",1000,1)
		height, elevation = calculate(elevation, speed, distance, wind_direction, difficulty) 

		#Displays the result of the shot
		if height<1:
			print("The shot was too near") 
		elif height>8:	
			print("The shot was too far")
		else:
			print("You hit the wall!!")	
			wall, wall_detail,z = determine_hit(wall, wall_detail, int(height), elevation, speed)

		#Determines whether the wall has moved
		#If it does, the distance changes.
		move_chance = randint(0,10)
		print(move_chance)
		if move_chance<2:
			print("The wall has moved")
			distance = randint(21,101)
			turn += 1

	return False

#Opaque Mathematical formulae that determines the result of the
#hit, and how much of the wall has been damaged
def determine_hit(wall, wall_detail,height,elevation,speed):

	wall,z = determine_damage(wall, wall_detail)
	wall[wall_detail[height]-1][height]=0

	if int(speed)*math.cos(elevation)>50: 
		wall[wall_detail[height]-2][height]=0

	if randint(0,10)>5 and height != 1:
		wall[wall_detail[1]][1]=9
	if randint(0,10)>5 and height>5 and height<7:
		wall[wall_detail[height+1]][height+1]=0

	for y in range(2,8):
		if randint(0,10)<5:
			wall[wall_detail[y]-1][y] = 0
	
	wall,z = determine_damage(wall, wall_detail)

	return wall, wall_detail,z
	
#This function was called twice. It looks as if it determines
#The winning condition as well.
def determine_damage(wall, wall_detail):

	for y in range(wall_height):
		x = 0
		z = 0
		while x<8:
			if wall[x][y] == 0 or x==7:
				wall_detail[y]=x
				if x == 1:
					z == 1
				x=9	
			else:
				x+=1
	return wall, z

if __name__ == '__main__':
	start_game()
