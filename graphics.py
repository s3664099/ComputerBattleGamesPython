"""
Title: Graphics Package
Translator: David Sarkies
Version: 1
Date: 8 October 2022

This file holds a series of functions that enable graphical displays using pygame.

To install pygame you need to do the following:

pip3 install pygame
"""

import pygame

#Initialises the PyGame library and creates the window with the caption being the title of the game
pygame.init()
display_width = 800
display_height = 600
clock = pygame.time.Clock()	
white = (255,255,255)

def display_screen():
	gameDisplay = pygame.display.set_mode((display_width,display_height))
	return gameDisplay

#Sets the caption of the screen
def set_caption(title):
	pygame.display.set_caption(title)

#Creates the icon
def create_icon(image):
	return pygame.image.load(image)

#Transforms the icon
def transform_icon(icon):
	return pygame.transform.scale(icon, (40,40))

#Displays the icon on the frame
def display_icon(icon,x,y,gameDisplay):
	gameDisplay.blit(icon, (x,y))

#Displays a message on the screen
def message_display(text ,display,size,textPosition):
	display_width = 800
	display_height = 600

	#Sets the text font	
	largeText = pygame.font.Font('freesansbold.ttf',size)

	#Creates the text objects
	TextSurf, TextRect = text_objects(text, largeText)

	if textPosition == "centre":
		#centers the text
		TextRect.center = ((display_width/2),(display_height/2))
	elif textPosition == "bottom":
		TextRect.center = ((display_width/2),display_height-100)

	#This updates the screen, and sleeps for two seconds
	get_display(display).blit(TextSurf, TextRect)
	pygame.display.update()
	pygame.time.wait(2000)

#These creates and displays a text object
def text_objects(text, font):
	textSurface = font.render(text, True, white)
	return textSurface, textSurface.get_rect()

def get_width():
	return display_width

def get_height():
	return display_height

def get_clock():
	return clock

def get_display(gameDisplay):
	return gameDisplay