#!/usr/bin/python3

"""
Title: Missile!
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 1.1
Date: 21 March 2021
Updated Date: 15 October 2022
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTVUExUjFhTURCSU0/view

This is the final game in the Computer Battlegames Book, and can be found on page 30. The difference with
this game is that there is a separate listing for each of the computers since it makes use of graphics and
sound. As such, I decided to rewrite the game using PyGame. I initially tried using tklinter, but it turned
out that PyGame is much better suited for it. Further, the problems that I faced with $INKEY don't exist
when you use PyGame.

You need to install PyGame to execute this game, and it can be done as follows:

pip3 install pygame

The functionality of the game is similar to what is listed, but quite a lot is different. I have to create
a window to hold the game, and as the game loops, it monitors for a key press. You have three missiles
and you need to hit the plane that is flying across the top of the screen (though the position is somewhat
random). It you hit the plane you win, but if you miss, you lose.

<div>Icons made by <a href="" title="itim2101">itim2101</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
"""

import pygame
import random
import util
import graphics

start_position = random.uniform(0,0.6) 
black = (0,0,0)
white = (255,255,255)

#Sets the icons that represent the plane, and the missiles
jetImg = graphics.create_icon('jet.png')
missileImg = graphics.create_icon('missile.png')
missileImg = graphics.transform_icon(missileImg)
text_size = 50

def main_game():

	graphics.set_caption("Missile!")
	display = graphics.display_screen()

	#Variables that set the starting position of the jet
	jet_x = (graphics.get_width() * 0)
	jet_y = (graphics.get_height() * start_position)

	#Variables that display the starting position of the missiles
	missile_y = [graphics.get_height() * 0.9,graphics.get_height() * 0.9,graphics.get_height() * 0.9]
	missile_x = [graphics.get_width() * 0.3,graphics.get_width() * 0.6,graphics.get_width() * 0.9]
	missile_launch = [False, False, False]

	#Stores the missile that is to be fired
	miss_no = 0

	#Flag to determine whether the game has ended
	crashed = False

	#Main game loop
	while not crashed:

		#Listens for events
		for event in pygame.event.get():
		
			#Checks to see if the player has ended the game
			#That is, pressed the x in the top right corner
			if event.type == pygame.QUIT:
				crashed = True
		
			#Listens for a key press and fires the missile if there is one
			if event.type == pygame.KEYDOWN and miss_no<3:
				missile_launch[miss_no] = True	
				miss_no += 1

		#Sets the background colour and displays the jet.
		display.fill(black)
		graphics.display_icon(jetImg,jet_x,jet_y,display)

		#Moves the jet across the screen
		jet_x += 1

		#Displays the missiles
		for x in range(3):

			#Checks to see if the missiles has been launched
			#And moves it if it has
			if missile_launch[x] == True:
				missile_y[x] -= 2
			graphics.display_icon(missileImg,missile_x[x],missile_y[x],display)

			#Detects whether the missile has hit the plane, and ends the game
			#If it has		
			if missile_x[x] > jet_x-20 and missile_x[x] < jet_x +20:
				if missile_y[x] > jet_y -20 and missile_y[x] < jet_y +20:
					graphics.message_display("You hit him!",display,text_size,"centre")
					crashed = True	

		#Checks to see if the jet has left the screen and ends the game
		#if it has
		if jet_x > graphics.get_width():
			graphics.message_display("You Missed!", display,text_size,"centre")
			crashed = True 

		pygame.display.update()
		graphics.get_clock().tick(60)

	#Delays closing the screen
	pygame.time.wait(1000)

def instructions():

	print("Missile!")
	print("========")
	print("You have three missile bases, each capable of launching one missile.")
	print("When you see a plane approaching, you must judge its height and speed")
	print("and fire your missiles at it one by one. Your missiles are launched by")
	print("pressing any key. The first time you press launches the left-hand one,")
	print("second time the middle one and third time the right-hand one.")
	print("See how many enemy planes you can shoot down.")
	print()
	input("Press enter to continue")

#Starts the game by asking instructions and creates a game loop
def start_game():

	util.clear_screen()
	print("Missle!")

	if (util.ask_instructions() == True):
		instructions()

	replay = True

	while replay:

		main_game()

		#Kills the screen to ask the play again question
		pygame.quit()

		replay = util.play_again(replay)

if __name__ == '__main__':
	start_game()

