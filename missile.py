#!/usr/bin/python3

"""
<div>Icons made by <a href="" title="itim2101">itim2101</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
"""

import pygame
import random
import time

pygame.init()
display_width = 800
display_height = 600	

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Missile!!')

black = (0,0,0)
white = (255,255,255)
start_position = random.uniform(0,0.6) 

clock = pygame.time.Clock()
jetImg = pygame.image.load('jet.png')
missileImg = pygame.image.load('missile.png')
missileImg = pygame.transform.scale(missileImg, (40,40))


def jet(x,y):
	gameDisplay.blit(jetImg, (x,y))

def missile(x,y):
	gameDisplay.blit(missileImg, (x,y))	

def text_objects(text, font):
	textSurface = font.render(text, True, white)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()
	time.sleep(2)

def main_game():

	jet_x = (display_width * 0)
	jet_y = (display_height * start_position)

	missile_y = [display_height * 0.9,display_height * 0.9,display_height * 0.9]
	missile_x = [display_width * 0.3,display_width * 0.6,display_width * 0.9]
	missile_launch = [False, False, False]
	miss_no = 0
	crashed = False
	while not crashed:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True
		
			if event.type == pygame.KEYDOWN and miss_no<3:
				missile_launch[miss_no] = True	
				miss_no += 1

		gameDisplay.fill(black)
		jet(jet_x,jet_y)
		jet_x += 1

		for x in range(3):
			if missile_launch[x] == True:
				missile_y[x] -= 2
			missile(missile_x[x],missile_y[x])
		
			if missile_x[x] > jet_x-20 and missile_x[x] < jet_x +20:
				if missile_y[x] > jet_y -20 and missile_y[x] < jet_y +20:
					message_display("You hit him!")
					crashed = True	

		if jet_x > display_width:
			message_display("You Missed!")
			crashed = True 

		pygame.display.update()
		clock.tick(60)


if __name__ == '__main__':
	main_game()

pygame.quit()
quit()
