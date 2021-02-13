#!/usr/bin/env python3

"""
Title: Supersonic Bomber
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 1
Date: 13 February 20201
Source: Source: https://drive.google.com/file/d/0Bxv0SsvibDMTVUExUjFhTURCSU0/view



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
		for z in range(cities[y]):
			city_graph += "**"
		print(city_graph)
	return cities, highest_pop+1

def main_game():

	util.clear_screen()
	print("Supersonic Bomber")
	score = 0
	cities = []
	time.sleep(1)
	no_cities = 5

	for x in range (10,0,-1):
		cities.clear()
		cities,highest_pop = set_up(cities, no_cities)			
		score = get_input(highest_pop,score,x)

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
			

if __name__ == '__main__':
	main_game()
