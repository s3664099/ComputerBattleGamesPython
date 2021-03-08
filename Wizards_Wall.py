#!/usr/bin/env python3

import util

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


if __name__ == '__main__':
	start_game()
