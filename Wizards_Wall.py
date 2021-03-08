#!/usr/bin/env python3

import util
import time
import math
from random import randint

wall_length = 8
wall_height = 8

def set_up():
	wall = [[0 for x in range(wall_length)] for y in range(wall_height)]
	wall_detail = [0 for y in range(wall_height)]
	
	for x in range(wall_length):
		for y in range(wall_height):
			wall[x][y] = 4 
	return wall, wall_detail

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

def press_enter():
	x = input("<<press Return to continue>>")

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
	
def start_game():
	util.clear_screen()
	print("The Wizard's Wall")
	correct = False

	while not correct:
		response = input("Do you want instructions? ")

		if response.lower()[:1] == "y":
			display_instructions()
			correct = True
		elif response.lower()[:1] == "n":
			correct = True
		else:
			print("Please enter (Y)es or (N)o")

	difficulty = get_difficulty()
	wall, wall_detail = set_up() 
	result = main_game(difficulty,wall, wall_detail)

	if result == True:
		print("You have managed to break a hole in the wizard's wall")
		print("You have beaten his magic powers, and freed his victims")
	else:
		print("You have been turned into stone")
		print("You are now a part of the wizard's wall")
		print("Too bad, so sad.")

def display_wall(wall):
	time.sleep(1)
	util.clear_screen()
	
	for y in range(7,0,-1):
		wall_display = ""
		for x in range (8):
			wall_display += str(wall[x][y])
		print(wall_display)

def wind():
	
	wind = randint(-20,20)
	if wind<0:
		print("Wind is blowing to the right")
	elif wind>0:
		print("Wind is blowing to the left")
	else:
		print("There is no wind")		
	return wind	

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
def calculate(elevation, speed, distance, wind_direction, difficulty):
	elevation = int(elevation)/180*3.1416
	dw = int(distance)-int(wind_direction)
	dwexp = (5*(dw)**2) 
	elecos = (int(speed)*math.cos(elevation))**2
	height = math.tan(elevation)*dw-dwexp/elecos
	height = (height/int(difficulty))

	return height, elevation

def main_game(difficulty,wall, wall_detail):
	distance = randint(21,101)
	z = 0
	turn = 0
	
	while turn < 3:
		display_wall(wall)
		if z == 1:
			return True
		print("You are {} yards away".format(distance))
		wind_direction = wind()
		elevation = get_value("elevation",90,1)
		speed = get_value("speed",1000,1)
		height, elevation = calculate(elevation, speed, distance, wind_direction, difficulty) 
		if height<1:
			print("The shot was too near") 
		elif height>8:	
			print("The shot was too far")
		else:
			print("You hit the wall!!")	
			wall, wall_detail,z = determine_hit(wall, wall_detail, int(height), elevation, speed)

		move_chance = randint(0,10)
		print(move_chance)
		if move_chance<2:
			print("The wall has moved")
			distance = randint(21,101)
			turn += 1

	return False

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
