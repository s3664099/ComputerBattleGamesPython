#!/usr/bin/python3

"""
Title: Missile!
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 1
Date: 21 March 2021
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
import time

#Initialises the PyGame library and creates the window with the caption being the title of the game
pygame.init()
display_width = 800
display_height = 600	
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Missile!!')

black = (0,0,0)
white = (255,255,255)
start_position = random.uniform(0,0.6) 
clock = pygame.time.Clock()

#Sets the icons that represent the plane, and the missiles
jetImg = pygame.image.load('jet.png')
missileImg = pygame.image.load('missile.png')
missileImg = pygame.transform.scale(missileImg, (40,40))

#Function that displays the jet
def jet(x,y):
	gameDisplay.blit(jetImg, (x,y))

#Function that displays the missiles
def missile(x,y):
	gameDisplay.blit(missileImg, (x,y))	

#These two functions creates and displays a text object
def text_objects(text, font):
	textSurface = font.render(text, True, white)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2),(display_height/2))

	#This updates the screen, and sleeps for two seconds
	gameDisplay.blit(TextSurf, TextRect)
	pygame.display.update()
	time.sleep(2)

def main_game():

	#Variables that set the starting position of the jet
	jet_x = (display_width * 0)
	jet_y = (display_height * start_position)

	#Variables that display the starting position of the missiles
	missile_y = [display_height * 0.9,display_height * 0.9,display_height * 0.9]
	missile_x = [display_width * 0.3,display_width * 0.6,display_width * 0.9]
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
		gameDisplay.fill(black)
		jet(jet_x,jet_y)

		#Moves the jet across the screen
		jet_x += 1

		#Displays the missiles
		for x in range(3):

			#Checks to see if the missiles has been launched
			#And moves it if it has
			if missile_launch[x] == True:
				missile_y[x] -= 2
			missile(missile_x[x],missile_y[x])

			#Detects whether the missile has hit the plane, and ends the game
			#If it has		
			if missile_x[x] > jet_x-20 and missile_x[x] < jet_x +20:
				if missile_y[x] > jet_y -20 and missile_y[x] < jet_y +20:
					message_display("You hit him!")
					crashed = True	

		#Checks to see if the jet has left the screen and ends the game
		#if it has
		if jet_x > display_width:
			message_display("You Missed!")
			crashed = True 

		pygame.display.update()
		clock.tick(60)


if __name__ == '__main__':
	main_game()

pygame.quit()
quit()
