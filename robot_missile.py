#!/usr/bin/env python3

"""
Title: Robot Missile
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 0
Date: 15 October 2022
Source: Source: https://drive.google.com/file/d/0Bxv0SsvibDMTVUExUjFhTURCSU0/view

This game can be found on page 4 of Computer Battle Games, and it a python3 translation.
"""

import util
from random import randint

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def instructions():

	util.clear_screen()
	print("Robot Missile")
	print("===== =======")
	print("The year is 2582 and the people of Earth are in the midst of a battle against the Robots.")
	print("A lethal Robot Missile has just landed and everyone is depending on you to find the secret")
	print("code which unlocks its defuse mechanism. If you fail, the entire Earth Command Headquarters")
	print("will be blown up. Your computer knows what the code letter is. You must type in your guess and")
	print("it will tell you whether the code letter is earlier or later in the alphabet. You have four")
	print("chances to find the correct letter before the missile blows up.")
	print()

def get_letter():

	letter = randint(0,25)
	return alphabet[letter]

def main_game(letter):

	print(letter)
	input("Press enter to continue")


def start_game():

	"""
	util.clear_screen()
	print("Robot Missile")

	if (util.ask_instructions() == True):
		instructions()
	else:
		print()
		print("Type the correct code letter (A-Z)")
		print("to defuse the missile")
		print("you have 4 changes")

	input("Press enter to continue")
	"""

	while True:
		main_game(get_letter())

if __name__ == '__main__':
	start_game()