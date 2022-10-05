from os import system
from time import sleep
from threading import Thread
import sys
import random

#Clears the screen
def clear():
	_ = system('clear')

#Function to get a random number between 1 and 3
def get_random():
	number = 1
	number = random.randint(number,number+2)
	return number

#Thread to manage the bad guy
def badguy():

	#Sets a global variable to determine
	#Whether the bad guy has shot
    global shot 
    shot = False

    delay = get_random()
    sleep(delay)

    #Checks to see if you have shot
    if answer != None:
        return

    print ("\nHe Draws ...")

    #Loop to control the shooting
    #If he hits, it ends, if he misses it goes around again
    while shot == False:
        delay = get_random()
        sleep(delay)
        shot = True

        if answer != None:
            return

        if check_missed() == True:
        	print("And shoots ...")
        	print("And misses!")
        	shot = False

    print ("And shoots ....")
    print ("You are dead!")
    quit()

#Function to check to see if either you or he has missed
def check_missed():

	missed = False
	hit = get_random()

	print(hit)

	if hit == 2:
		missed = True

	return missed

#Main shooting function
def draw():

	#Sets a global variable to see whether you have shot
	global answer
	answer = None

	#Creates a thread to handle the bad guy
	Thread(target = badguy).start()

	#Loop to see whether you have hit him
	#If you have missed it goes through again
	while answer == None:

		answer = input("Draw:")

		if shot == False:

			if check_missed() == True:

				print("You missed")
				answer = None

	if shot == False:
		print("You shot first")
		print("You killed him")
	quit()

#Main title function
def main():
	clear()
	print("Cowboy Shootout -")
	sleep(2)
	print("You are back to back")
	sleep(2)
	print("Take ten paces")

	for i in range (10):
		print("--")
		sleep(2)

	draw()

if __name__ == "__main__":
	main()
