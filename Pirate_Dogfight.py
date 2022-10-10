#!/usr/bin/env python3

"""
Title: Pirate Dogfight
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 1.1
Date: 6 October 2022
Source: Source: https://drive.google.com/file/d/0Bxv0SsvibDMTVUExUjFhTURCSU0/view

This game can be found on page 20 of Computer Battle Games, and it a python3 translation. Due to the use of the $inkey/$get command in this game, it will no doubt be tricky to convert it into any of the other languages.

The goal of the game is to shoot down the opponent and you do this by increasing
/decreasing your speed until you are next to him/her, and then you shoot.
A display is on the screen to show your relative position to your oppenant. If
your opponent gets too far away from you (20 units), you will lose the game

I have changed the text, and I have also added code so that if you are too far
away from your opponent, you cannot shoot them. Further, you cannot shoot
your opponent if you are in front.

The difficulty is the use of the $Inkey. I have used a timed input, which
expires after a second, however you need to press enter otherwise the command
will not register.

I experimented with the keyboard package for python, which detects a keypress,
but unfortunately you can only use it if the program is running in root mode.
It also would print the keypress to the screen, and didn't always detect it.
However, it was the need to execute in root mode that I ended up dropping it.

The controls are as follows:
a - accellerate
d - decellerate
f - fire

Player Jet:
<a href="https://www.flaticon.com/free-icons/jet-plane" title="jet plane icons">Jet plane icons created by imaginationlol - Flaticon</a>

Enemy Jet:
<a href="https://www.flaticon.com/free-icons/jet" title="jet icons">Jet icons created by Creaticca Creative Agency - Flaticon</a>
"""

import util
import time
from random import randint
import pygame
import graphics

#Sets the screen width based on an ubuntu terminal
display_width = graphics.display_width
display_height = graphics.display_height
black = (0,0,0)

#Sets the jets
playerJetImg = graphics.create_icon('playerJet.png')
enemyJetImg = graphics.create_icon('enemyJet.png')
playerJetImg = graphics.transform_icon(playerJetImg)
enemyJetImg = graphics.transform_icon(enemyJetImg)

#Displays the position of the planes. The opponent is always
#in the centre of the screen
def set_position(height,distance):

	jet_x = (display_width*0.5+distance)
	jet_y = (display_height*0.5+height)

	return jet_x,jet_y
	
#Gets the distance of the plane from the edge of the screen
def get_distance(length):
	length = int(length)
	display = ""

	for x in range(length):
		display +=" "

	return display

#Checks your position relative to the opponent
def check_position(distance):
	if distance<0:
		return "Behind"
	elif distance >0:
		return "In Front"
	else:
		return "Level"

#Checks your speed relative to the opponent
def check_speed(velocity):
	if velocity > 0:
		return "Going faster"
	elif velocity < 0:
		return "Going slower"
	else:
		return "The same speed"	

#Gets the players move
def get_move(velocity, distance,display):

	#Checks to see if you are too far away from the oppoent
	if abs(distance)>20:
		return 1,distance,velocity

	"""
	#Gets the input from the player
	key = util.input_with_timeout_no_comment(">",2)

	#Executes the players command
	if key == 'a':
		velocity += 1
	elif key == 'd':
		velocity -= 1
	elif key == 'f':

		#Executes the fire command and determines
		#The result
		print("Pew Pew Pew")
		result = fire(velocity,distance)
		if result == 1:
			print("Your shots fly over his wing, you are going too fast")
		elif result == 4:
			print("You are too far away, your shots fall short")
		elif result == 5:
			print("He's behind you. You can't hit him")
		elif result == 3:
			time.sleep(1)
			return result,distance,velocity
		else:
			time.sleep(1)
			return result,distance,velocity

	#Changes your position relative to the opponent
	distance = distance + velocity
	time.sleep(1)
	"""

	return 0,distance,velocity

#The fire function. Determines the response based on the positon
def fire(velocity,distance):

	#In front
	if distance>0:
		return 5

	#Too far behind
	elif distance<-2:
		return 4
	
	#Going too fast/slow
	elif abs(velocity)>2:
		return 1

	#Within striking distance, determines who hits who 
	else:
		if randint(1,10)>5:
			return 2
		else:
			return 3

def instructions():

	util.clear_screen()
	print("Pirate Dog-Fight")
	print("================")
	print("It's you against the Sky Pirate. He moves ahead, you accelerate - He")
	print("drops behind, you slow down. You must try to get level with him and then")
	print("you can fire, hoping that he won't be able to fire and hit you first.")
	print("Use the letter keys A to accelerate, D to decelerate and F to fire. Your")
	print("computer will tell you your speed and position relative to the pirate. You")
	print("will need to be ready to press the appropriate keys as soon as you press")
	print("RUN. Keep pressing A and D until you get level and then fire")
	print("** Note that you have to press enter after pressing the key")
	print()
	input("Press enter to continue")

def main_game():

	#Sets up the game and determines initial
	#velocity and position
	util.clear_screen()
	print("Pirate Dog-Fight")

	if (util.ask_instructions() == True):
		instructions()

	replay = True

	while replay:

		graphics.set_caption("Pirate Dog-Fight")
		display = graphics.display_screen()

		end_note = ""
		continuing = True
		velocity = randint(-5,5)
		distance = randint(1,4)*40

		print(distance)

		player_x,player_y = set_position(40,distance)
		enemy_x,enemy_y = set_position(0,0)

		#Game loop
		while continuing:

			#Clears the screen
			graphics.get_display(display).fill(black)

			graphics.display_icon(playerJetImg,player_x,player_y,display)
			graphics.display_icon(enemyJetImg,enemy_x,enemy_y,display)

			result,distance, velocity = get_move(velocity, distance,display)

			#Determines the result of the game
			if result == 1:
				end_note = "He got away"
				continuing = False
			elif result == 2:
				end_note = "You shot him down"
				continuing = False
			elif result == 3:
				end_note = "He shot you first"
				continuing = False

			pygame.display.update()
			graphics.get_clock().tick(60)

		print(end_note)

		replay = util.play_again(replay)

if __name__ == '__main__':
	main_game()
