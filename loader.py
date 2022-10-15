#!/usr/bin/env python3

import util
import time
import Robot_Invaders
import Secret_Weapon
import escape
import Pirate_Dogfight
import Supersonic_Bomber
import iceberg
import Wizards_Wall
import missile
import robot_missile
import vital_message

#Function that displays the games available, and allows the user to select them
def select_game():
	
	selecting = True

	#Creates a while loops to hold the menu to select the game
	while (selecting):
		util.clear_screen()
		print("1) Robot Missile")
		print("2) The Vital Message")
		print("3) Shootout *")
		print("4) Deset Tank Battle *")
		print("5) Battle at Traitor's Castle *")
		print("6) Robot Invaders")
		print("7) Secret Weapon")
		print("8) Escape!")
		print("9) Pirate Dogfight")
		print("10) Supersonic Bomber")
		print("11) Iceberg")
		print("12) Wizard's Wall")
		print("13) Missile!")
		print("X) Exit")
		print()
		print("Games marked with an asterix '*' haven't been incorporated yet")
		print()
		response = input()

		#Executes the players selection
		if response.upper() == 'X':

			#Ends the program by letting it run out
			selecting = False

		#Loads the games based on the selection
		elif response == '1':
			robot_missile.start_game()
		elif response == '2':
			vital_message.start_game()
		elif response  == '6':
			Robot_Invaders.main()
		elif response == '7':
			Secret_Weapon.main()
		elif response == '8':
			escape.main()
		elif response == '9':
			Pirate_Dogfight.main_game()
		elif response == '10':
			Supersonic_Bomber.main_game()
		elif response == '11':
			iceberg.setup_game()
		elif response == '12':
			Wizards_Wall.start_game()
		elif response == '13':
			missile.start_game()
		else:
			print("You have entered an incorrect option")
			time.sleep(5)

if __name__ == '__main__':
	select_game()

