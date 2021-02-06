#!/usr/bin/env python3

#Screen 75 spaces across - use that for image

import util
import time
from random import randint

def check_position(distance):
	if distance<0:
		return "Behind"
	elif distance >0:
		return "In Front"
	else:
		return "Level"

def check_speed(velocity):
	if velocity > 0:
		return "Going faster"
	elif velocity < 0:
		return "Going slower"
	else:
		return "The same speed"	

def get_move(velocity, distance):
	if abs(distance)>20:
		return 1,distance,velocity
	util.clear_screen()

	print ("You are: {} {}".format(check_position(distance), check_speed(velocity)))
	print(velocity, distance)
	key = util.input_with_timeout(">",1)
	print("key press {}".format(key))
	if key == 'a':
		velocity += 1
	elif key == 'd':
		velocity -= 1
	elif key == 'f':
		print("Pew Pew Pew")
		result = fire(velocity,distance)
		print("Result {}".format(result))
		result = 3
		if result == 1:
			print("Your shots fly over his wing, you are going too fast")
		elif result == 4:
			print("You are too far away, your shots fall short")
		elif result == 5:
			print("He's behind you. You can't hit him")
		elif result == 3:
			print("Hello {}".format(result))
			time.sleep(1)
			print("After Sleep")
			return result,distance,velocity
		else:
			print("Hello {}".format(result))
			time.sleep(1)
			print("After Sleep")
			return result,distance,velocity

	distance = distance + velocity
	time.sleep(1)

	return 0,distance,velocity


def fire(velocity,distance):

	if distance>0:
		return 5
	elif distance<-2:
		return 4
	elif abs(velocity)>2:
		return 1
	else:
		if randint(1,10)>5:
			return 2
		else:
			return 3

def main_game():

	end_note = ""
	continuing = True
	util.clear_screen()
	print("Pirate Dog-Fight")
	velocity = randint(-5,5)
	distance = randint(1,4)*-1

	while continuing:

		result,distance, velocity = get_move(velocity, distance)
		print(result)
		print(result, distance, velocity)

		if result == 1:
			end_note = "He got away"
			continuing = False
		elif result == 2:
			end_note = "You shot him down"
			continuing = False
		elif result == 3:
			end_note = "He shot you first"
			print("He shoots")
			continuing = False

	print(end_note)

if __name__ == '__main__':
	main_game()
