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
difficulty setting to make the game easier/harder. The difficulty setting
increases the number of 'population centres' as well as lowering the time
for the player to respond.
"""

import util
import time
from random import randint

#Sets up the round by setting the population of the cities
#and printing out the graphs. Determines the city with the highest
#population
def set_up(cities, no_cities):

	highest_pop = 0

	#Populates the cities and determines the one
	#With the highest population
	for y in range(no_cities):
		population = randint(1,10)
		cities.append(population)
		if cities[y]>cities[highest_pop]:
			highest_pop = y 

	util.clear_screen()

	#Prints out the graph showing the size
	#of the cities
	for y in range(no_cities):
		city_graph = str(y+1)+": "
		if (y+1)<10:
			city_graph +=" "
		for z in range(cities[y]):
			city_graph += "**"
		print(city_graph)

	#Returns the cities and the highest population
	return cities, highest_pop+1

#Instructions function
def instructions():

	util.clear_screen()
	print("You are on a lone supersonic bombing mission over the U.R.S. Your computer")
	print("shows graphs of Robot population based on infrared photographs relayed to it by")
	print("satellite. You only have time to attack one target in five, so you must quickly")
	print("select the one with the highest population of Robots and release one of")
	print("your 'Corrodarobe' bombs on it. (These contain a substance so corrosive it can")
	print("dissolve a Robot's body in seconds.) To release a bomb, press the number")
	print("key which corresponds to the number next to the graph of highest Robot")
	print("population. If there are two the same, choose the one with the lowest number.")
	print("Will you be a hero when you return to base?")
	print("")
	input("Press Enter to Continue")

#Main game function
def main_game():

	#Sets the initial variables and gets difficulty
	util.clear_screen()
	print("Supersonic Bomber\n\n")

	if (util.ask_instructions() == True):
		instructions()

	replay = True

	while replay:
		util.clear_screen()

		difficulty = set_difficulty()
		score = 0
		cities = []
		no_cities = 5
		time_diff = 2

		#Determines the difficulty settings
		if difficulty == "2":
			no_cities = 10
			time_diff = 1
		elif difficulty == "3":
			no_cities = 15
			time_diff = 0.5

		#Executes ten rounds for the game
		for x in range (10,0,-1):
			cities.clear()
			cities,highest_pop = set_up(cities, no_cities)			
			score = get_input(highest_pop,score,x*time_diff)

		#Tells the player their results
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

		replay = util.play_again(replay)
		
#Gets the player's input for the round
def get_input(highest_pop,score,level):

	keypress = util.input_with_timeout(">",level)

	#Checks to see if the player got the correct input
	#And adds one to score if so
	if keypress == str(highest_pop):
		score += 1
		print("Boom!")
	return score
			
#Sets the difficulty for the game
def set_difficulty():

	#Input loop, uses while true as will break out of
	#loop if input valid 
	while True:
		print("Please select difficulty level")
		print("1) Easy")
		print("2) Medium")
		print("3) Hard")
		difficulty = input("> ")

		#Validates the input. Returns if input is corrrect
		if difficulty == "1" or difficulty == "2" or difficulty == "3":
			return difficulty
		print("Please enter either 1, 2 or 3")


if __name__ == '__main__':
	main_game()
