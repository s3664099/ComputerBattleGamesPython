#!/usr/bin/env python3

"""
Title: Supersonic Bomber
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 1
Date: 13 February 20201
Source: Source: https://drive.google.com/file/d/0Bxv0SsvibDMTVUExUjFhTURCSU0/view

This game is located on page 22 of Computer Battle Games, and is a python3
translation. One again, due to the use of the $Inkey/Get command, I have used a
timed input, though this seems to be appropriate with this particular game.

The game will display a number of 'population centres' and you have to select
the one that has the highest population. You then must press the button
corresponding to the correct centre to get a point. If two are the same then you
select the lowest one on the list.

This game was pretty straight forward to transfer into python, though the timed
input might be a bit tricky with other languages.

I have added better responses for the completion, and have also added a 
difficulty setting to make the game easier/harder.

"""

import util
import time
from random import randint


def set_up(cities, no_cities):
	highest_pop = 0
	for y in range(no_cities):
		population = randint(1,10)
		cities.append(population)
		if cities[y]>cities[highest_pop]:
			highest_pop = y 

	util.clear_screen()
	for y in range(no_cities):
		city_graph = str(y+1)+": "
		if (y+1)<10:
			city_graph +=" "
		for z in range(cities[y]):
			city_graph += "**"
		print(city_graph)
	return cities, highest_pop+1

def main_game():

	util.clear_screen()
	print("Supersonic Bomber\n\n")
	difficulty = set_difficulty()
	score = 0
	cities = []
	no_cities = 5
	time_diff = 2

	if difficulty == "2":
		no_cities = 10
		time_diff = 1
	elif difficulty == "3":
		no_cities = 15
		time_diff = 0.5

	for x in range (10,0,-1):
		cities.clear()
		cities,highest_pop = set_up(cities, no_cities)			
		score = get_input(highest_pop,score,x*time_diff)

	print("You hit {} out of 10".format(score))
	print("high density targets")
	if score == 10:
		print("You are a champion!")
	elif score >4:
		print("Good, but not good enough")
	elif score >0:
		print("You could definitely do better")
	else:
		print("Hey, you suck big time")
		
def get_input(highest_pop,score,level):

	keypress = util.input_with_timeout(">",level)
	print(highest_pop)
	print(keypress)
	if keypress == str(highest_pop):
		score += 1
		print("Boom!")
	return score
			
def set_difficulty():

	while True:
		print("Please select difficulty level")
		print("1) Easy")
		print("2) Medium")
		print("3) Hard")
		difficulty = input("> ")

		if difficulty == "1" or difficulty == "2" or difficulty == "3":
			return difficulty
		print("Please enter either 1, 2 or 3")


if __name__ == '__main__':
	main_game()
