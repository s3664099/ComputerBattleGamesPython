#!/usr/bin/env python3

import util
from random import randint

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

def set_positions(game_map, ship):
	ship_placed = False
	while(not ship_placed):
		ship_x = randint(0,map_size-1)
		ship_y = randint(0,map_size-1)
		if (game_map[ship_x][ship_y] == 0):
			game_map[ship_x][ship_y] = ship
			return ship_x, ship_y
	
def build_map(game_map):

	global enemy_x 

	global enemy_y
	global player_x
	global player_y

	for x in range (no_icebergs):
		x=randint(0,map_size-1)
		y=randint(0,map_size-1)
		game_map[x][y]=1

	enemy_x, enemy_y = set_positions(game_map,enemy)
	player_x, player_y = set_positions(game_map,player)

	return game_map

def print_map(game_map):

	print("==========")
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

def move_enemy():

	global enemy_x 
	global enemy_y
	global player_x
	global player_y

	if player_x - enemy_x < 0:
		enemy_x -=1
	elif player_x - enemy_x > 0:
		enemy_x +=1
	
	if player_y - enemy_y <0:
		enemy_y -=1
	elif player_y-enemy_y >0:
		enemy_y +=1 

def main_game(game_map):

	global enemy	
	game_on = True
	print_map(game_map)

	while(game_on):
		game_map[player_x][player_y] = 0
		get_command(game_map)
		
		if game_map[player_x][player_y] == 1: 
			print("Crunch!!! You've crashed into an iceberg!")
			return False
		elif game_map[player_x][player_y] == enemy:
			print("You have got too close to the enemy, you've been boarded")
			return False

		game_map[player_x][player_y] = player

		game_map[enemy_x][enemy_y] = 0
		move_enemy()

		if game_map[enemy_x][enemy_y] == 1:
			print("Crash! The enemy has crashed into an iceberg!")
			return True

		game_map[enemy_x][enemy_y]=enemy		

		if game_map[player_x][player_y] == enemy:
			print("The enemy ship has caught you and boarded you")
			return False

		util.clear_screen()
		print_map(game_map)

def get_command(game_map):

	global enemy_x 
	global enemy_y
	global player_x
	global player_y

	response = 0

	while(True):

		print("Moves: n,s,e,w")
		print("q: quits game")
		print("0: remain in position")
		move = input("Please enter your move: ")
		
		if move == 'n':
			if player_x >0:
				player_x -=1 
				return 
			else:
				response = 2
		elif move == 's':
			if player_x <map_size-1:
				player_x +=1 
				return
			else:
				response = 2
		elif move == 'e':
			if player_y <map_size-1:
				player_y +=1 
				return
			else:
				response = 2
		elif move == 'w':
			if player_y >0: 
				player_y -=1 
				return
			else:
				response = 2
		elif move == 'q':
			quit()
		elif move == '0':
			return
		else:
			response = 1

		if response == 2:
			print("Invalid move: you can't leave the map")
		else:
			print("Invalid move: plese enter n,s,e or w") 


def setup_game():

	util.clear_screen()
	game_map = [[0 for x in range(map_size)] for y in range(map_size)] 
	print('Iceberg')
	game_map = build_map(game_map)
	result = main_game(game_map)
	
	if not result:
		print("You Lose!")
	else:
		print("You win!")

if __name__ == '__main__':
	setup_game()
