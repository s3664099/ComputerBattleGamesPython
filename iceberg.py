#!/usr/bin/env python3

"""
Title: Iceberg
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 1
Date: 27 February 2021
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTVUExUjFhTURCSU0/view

This game is from page 24 of computer battlegames and is a python translation
of a basic game. However, since the $GET isn't used in this game, it could
be written in other languages quite easily.

I have used global variables in this game since there are a lot of changes to
some of these variables, namely the position of the player and the enemy.
However, this could also be solved using a dictionary where the important
information is stored so that the specific python characteristics (such as
returning multiple variables) isn't available.

The size of the map can be changed by adjusting the map_size variable, and the
number of icebergs can be changed by adjusting the min_icebergs and max-icebergs
variables.

I have changed some of the text, and also added commands that includes standing
still, and also quitting out of the game if the player so wants to.
"""

import util
from random import randint

#Global Variables
min_icebergs = 4
max_icebergs = 11
no_icebergs = randint(min_icebergs,max_icebergs)
map_size = 8
enemy_x = 0
enemy_y = 0
enemy = 3
player_x = 0
player_y = 0
player = 4

#This function sets the location of the ship. The game map is
#passed through, as well as the ship to be set
def set_positions(game_map, ship):

	ship_placed = False

	#The function loops while the ship is being placed
	#It makes sure that the ship is placed in an empty
	#place (no iceberg or other ship
	while(not ship_placed):
		ship_x = randint(0,map_size-1)
		ship_y = randint(0,map_size-1)
		if (game_map[ship_x][ship_y] == 0):
			game_map[ship_x][ship_y] = ship
			return ship_x, ship_y
	
#The function that builds the map
def build_map(game_map):

	global enemy_x 
	global enemy_y
	global player_x
	global player_y

	#Sets the location of the icebergs
	#The number of icebergs is a random number set at initialisation
	for x in range (no_icebergs):
		x=randint(0,map_size-1)
		y=randint(0,map_size-1)
		game_map[x][y]=1

	#Sets the location of the player and enemy ships
	enemy_x, enemy_y = set_positions(game_map,enemy)
	player_x, player_y = set_positions(game_map,player)

	return game_map

#Fuction that prints the game map. It also includes a border.
def print_map(game_map):

	print("==========")

	#The function builds each of the lines of the map
	#And then prints out the lines
	for x in range (map_size):
		map_line = "|"
		for y in range(map_size):
			if game_map[x][y] == 0:
				map_line += " "
			elif game_map[x][y] == 1:
				map_line += "."
			elif game_map[x][y] == 4:
				map_line += "y"
			elif game_map[x][y] == 3:
				map_line += "e"
		map_line += "|"
		print(map_line)
	
	print("==========")

#Function that moves the enemy ship
def move_enemy():

	global enemy_x 
	global enemy_y
	global player_x
	global player_y

	#The function determine the location of the player
	#and moves the enemy one spot towards it
	if player_x - enemy_x < 0:
		enemy_x -=1
	elif player_x - enemy_x > 0:
		enemy_x +=1
	
	if player_y - enemy_y <0:
		enemy_y -=1
	elif player_y-enemy_y >0:
		enemy_y +=1 

#The main game loop
def main_game(game_map):

	#The initial starting position is displayed
	global enemy	
	game_on = True
	print_map(game_map)

	while(game_on):

		#The player's position is cleared and
		#the player's command is requested
		game_map[player_x][player_y] = 0
		get_command(game_map)
		
		#Checks to see if the player has hit anything
		#If so, the game is ended.
		if game_map[player_x][player_y] == 1: 
			print("Crunch!!! You've crashed into an iceberg!")
			return False
		elif game_map[player_x][player_y] == enemy:
			print("You have got too close to the enemy, you've been boarded")
			return False

		#The player's new position is recorded on the map
		game_map[player_x][player_y] = player

		#The enemy then moves
		game_map[enemy_x][enemy_y] = 0
		move_enemy()

		#Checks to see if the enemy has hit an iceberg
		#If so, the player wins
		if game_map[enemy_x][enemy_y] == 1:
			print("Crash! The enemy has crashed into an iceberg!")
			return True

		#Checks to see if the enemy has caught the player
		#If so, the player loses
		game_map[enemy_x][enemy_y]=enemy		
		if game_map[player_x][player_y] == enemy:
			print("The enemy ship has caught you and boarded you")
			return False

		util.clear_screen()
		print_map(game_map)

#Gets the player's command
def get_command(game_map):

	global player_x
	global player_y

	response = 0

	#Creates a loop so that the player has to enter the correct
	#Command
	while(True):

		print("Moves: n,s,e,w")
		print("q: quits game")
		print("0: remain in position")
		move = input("Please enter your move: ")
	
		#Checks to see if the player has attempted to
		#move off of the map. Also checks to see if the
		#command is valid	

		#North
		if move == 'n':
			if player_x >0:
				player_x -=1 
				return 
			else:
				response = 2
		#South
		elif move == 's':
			if player_x <map_size-1:
				player_x +=1 
				return
			else:
				response = 2
		#East
		elif move == 'e':
			if player_y <map_size-1:
				player_y +=1 
				return
			else:
				response = 2
		#West
		elif move == 'w':
			if player_y >0: 
				player_y -=1 
				return
			else:
				response = 2

		#Quit Command
		elif move == 'q':
			quit()

		#Stand Still command
		elif move == '0':
			return
		else:
			response = 1

		#If the command is invalid, an error is printed
		if response == 2:
			print("Invalid move: you can't leave the map")
		else:
			print("Invalid move: plese enter n,s,e or w") 

#Sets up the game
def setup_game():

	util.clear_screen()
	print('Iceberg')

	#Builds the game map and populates it.
	game_map = [[0 for x in range(map_size)] for y in range(map_size)] 
	game_map = build_map(game_map)

	#Starts the main game loop
	result = main_game(game_map)
	
	#Displays the result of the game
	if not result:
		print("You Lose!")
	else:
		print("You win!")

if __name__ == '__main__':
	setup_game()
