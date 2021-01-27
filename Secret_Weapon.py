#!/usr/bin/env python3

import util
import math
from random import randint

"""

"""

def get_difficulty():

	correct = False

	while not correct:
		print("\nEnter Difficulty")
		difficulty = input(">> ")

		try:
			if int(difficulty)>3:
				return int(difficulty)
			print("Please enter a difficulty greater than 3")
		except:
			print("Please enter an integer")

def get_move(statement):

	while True:

		try:
			player_try = input(statement)
			player_try = int(player_try)

			return player_try
		except:
			print("Please enter integers")

def main_loop(difficulty, x_coord, y_coord):

	score = 0

	for x in range(difficulty+5):
	
		x_try = get_move("Select X coordinate: ")
		y_try = get_move("Select Y coordinate: ")
		hit = math.sqrt(((x_coord-x_try)**2)+((y_coord-y_try)**2))

		if hit == 0:
			score += 10
			return "Destroyed It", score
		elif hit <= 3:
			score += 1
			print("Close")
		else:
			print("Miss")

	return "The Robots have seen you - AGGGHHHH ....", score

def main():

	util.clear_screen()
	print("Secret Weapon")
	difficulty = get_difficulty()
	x_coord = randint(0,difficulty+1)
	y_coord = randint(0,difficulty+1)

	result, score = main_loop(difficulty,x_coord,y_coord)

	print(result)
	print("Your score is: {}".format(score))

if __name__ == '__main__':
	main()


