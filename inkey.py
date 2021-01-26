from readchar import readchar
from sys import stdin, stdout
from select import select

def inkey():
	if select([stdin,],[],[],0.0)[0]:
		return readchar()
	return ''

a = ''
timer = 0
while a != 'Q':
	a = inkey()
	if a != '':
		stdout.write(a)
		stdout.flush()
		if ord(a) == 13:
			stdout.write("\n")
	timer += 1
	if timer > 1000000:
		print("Type faster, human!")
		timer = 0