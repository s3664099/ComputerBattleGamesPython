from readchar import readchar
from sys import stdout

a = ' '
while ord(a) not in [3,24,27]:

	for x in range(5):
	    a = readchar()
	    if (a != ""):
		    stdout.write(a)
		    stdout.flush()
		    print(a)
		    if ord(a) == 13:
		        stdout.write("\n")
	print("Ping")