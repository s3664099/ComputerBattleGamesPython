#!/usr/bin/env python3

import util
from random import randint

"""
Title: Escape
Author: Daniel Isaaman & Jenny Tyler
Translater: David Sarkies 
Version: 1
Date: 27/1/2021
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTVUExUjFhTURCSU0/view


"""

guess_range = 5
danger_range = 40
frequency_range = 100


def get_input():

	while True:
		guess = input("Guess: ")

		try:
			return int(guess)
		except:
			print("Please enter an integer")

def check_guess(frequency, guess):

	if abs(frequency-guess)<guess_range:
		return 1
	elif frequency-guess > danger_range:
		return 2
	elif guess-frequency > danger_range:
		return 3
	else:
		return 0


def game_loop(frequency):
	low_frequency = 1
	high_frequency = 1

	for x in range(5):
		guess = get_input()

		result = check_guess(frequency, guess)

		if result == 1:
			return ("You've done it, you've shut down the robot"), False
		elif result == 2:

			if low_frequency == 2:
				return ("Too low - the building collapses"), True

			print("Too low, be careful, the building is shuddering")
			low_frequency = 2

		elif result == 3:

			if high_frequency == 2:
				return ("Too high, your head explodes"), True

			print("Too high, be careful, your head is starting to hurt")
			high_frequency = 2

		else:

			print("No discernable effect")

	return("You took too long. The robots have tortured you to death, the frequency was {}".format(frequency))

def main():
	util.clear_screen()
	print("Escape")
	print("There are three robots to take out. Guess their frequencies")
	robot = 0
	end_message = "You have shut down all three robots. You can escape"

	while robot < 3:
		print("Robot number {}".format(robot+1))
		frequency = randint(1,frequency_range)
		result, death = game_loop(frequency)

		if death == True:
			end_message = result
			robot = 5
		else:
			print(result)
			robot +=1

	print(end_message)


if __name__ == '__main__':
	main()
	