#!/usr/bin/env python3

"""
Title: Pirate Dogfight
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 2
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
https://www.flaticon.com/free-icons/jet-plane" Jet plane icons created by imaginationlol - Flaticon

Enemy Jet:
https://www.flaticon.com/free-icons/jet" Jet icons created by Creaticca Creative Agency - Flaticon

Bullets:
https://www.flaticon.com/free-icons/bullet Bullet icons created by Nikita Golubev - Flaticon

22 October 2022 - Added graphics to the game
"""

import util
from random import randint
import pygame
import graphics

#Sets the screen width based on an ubuntu terminal
display_width = graphics.display_width
display_height = graphics.display_height
black = (0,0,0)
delay = 500

#Sets the icons
playerJetImg = graphics.create_icon('playerJet.png')
enemyJetImg = graphics.create_icon('enemyJet.png')
bulletsImg = graphics.create_icon('bullets.png')
playerJetImg = graphics.transform_icon(playerJetImg)
enemyJetImg = graphics.transform_icon(enemyJetImg)
bulletsImg = graphics.transform_icon(bulletsImg)

#Displays the position of the planes. The opponent is always
#in the centre of the screen
def set_position(height,distance):

	jet_x = (display_width*0.5+distance)
	jet_y = (display_height*0.5+height)

	return jet_x,jet_y
	
#The fire function. Determines the response based on the positon
def fire(velocity,distance):

	#In front
	if distance>0:
		return 5,"He's behind you. You can't hit him"

	#Too far behind
	elif distance<-50:
		return 4,"You are too far away, your shots fall short"
	
	#Going too fast/slow
	elif abs(velocity)>20:
		return 1, "Your shots fly over his wing, you are going too fast"

	#Within striking distance, determines who hits who 
	else:
		if randint(1,10)>5:
			return 2, "You shot him down"
		else:
			return 3, "He shot you first"

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
	answer,replay = util.start_game("Pirate Dog-Fight")

	if (answer):
		instructions()

	while replay:

		graphics.set_caption("Pirate Dog-Fight")
		display = graphics.display_screen()

		continuing = True
		velocity = randint(-5,5)
		distance = randint(1,4)*40

		player_x,player_y = set_position(40,distance)
		enemy_x,enemy_y = set_position(0,0)

		#Game loop
		while continuing:

			#Clears the screen
			graphics.get_display(display).fill(black)

			#Displays the jets
			graphics.display_icon(playerJetImg,player_x,player_y,display)
			graphics.display_icon(enemyJetImg,enemy_x,enemy_y,display)

			firing = False

			#Registers the player input
			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					continuing = False

				#Keys for speeding the jet up, or slowing it down
				if event.type == pygame.KEYDOWN:

					if event.key == pygame.K_a:
						velocity +=1
					elif event.key == pygame.K_d:
						velocity -=1
					elif event.key == pygame.K_f:
						firing = True

			#Sets the new position of the player and the enemy
			enemy_x -= 10
			player_x -= velocity*10
			pygame.time.wait(delay)
			distance = enemy_x-player_x

			#Checks if the distance is too large, or either jet has hit the edge of the screen
			if (abs(distance)>500) or (player_x <0) or (enemy_x<0):
				graphics.message_display("He got away",display,50,"bottom")
				continuing = False

			#Has the player fired
			if (firing):

				#Sets the position of the bullet icons appearing on the screen
				bullet_position = player_x-10

				if velocity <0:
					bullet_position = player_x-50

				#Displays the bullet icons
				graphics.display_icon(bulletsImg,bullet_position,player_y,display)

				#Gets the result of the attack
				result, message = fire(velocity, distance)

				#Either one jet has been shot down, or missed
				if result == 2 or result == 3:
					graphics.message_display(message, display,25,"centre")
					continuing = False
				else:
					graphics.message_display(message, display,25,"bottom")
			
			#Redraws the screen
			pygame.display.update()
			graphics.get_clock().tick(60)

		pygame.quit()

		replay = util.play_again(replay)

if __name__ == '__main__':
	main_game()
