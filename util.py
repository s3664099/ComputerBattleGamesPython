from os import system
from inputimeout import inputimeout, TimeoutOccurred

"""
Title: Util.py
Author: David Sarkies
Version: 1
Date: 26/1/2021

This file holds functions that are likely to be used across multiple
programs. The clear screen fuction operates under unix-like operating systems.

TimeoutExpired, alarm_handler, and input_with_timeout are fuctions that are
designed to limit the amount of time the user has to input a response. Unfortunately
the user will need to press enter to record the response.

The following package is required:
https://pypi.org/project/inputimeout/
"""

def clear_screen():
	_ = system('clear')

#Exception that is called when the time limit expires
class TimeoutExpired(Exception):
	print("Time Out")

def alarm_handler(signum, frame):
	raise TimeoutExpired

#Timeout function. Takes a prompt and a time in seconds
#For the timeout
def input_with_timeout(prompt, timeout):
	
	keypress = ""

	#Waits for the user input
	try:
		keypress = inputimeout(prompt, timeout)

	#If the time limit expires an error is thrown.
	except TimeoutOccurred:
		pass
	return keypress
