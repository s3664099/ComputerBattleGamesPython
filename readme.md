# Computer Battle Games

These files are a translation of an old programming book from the 1980s
called 'Computer Battle Games'. The idea was to teach children programming
using basic. Due to multiple different systems back in the day there were marks
advising of when the code needed to be changed for a specific machine.

I used a Commodore 64 for my machine.

However, I have decided to translate them into modern computer languages. Initially
I was going to do it using C++, Java, and Python however issues arose that made me
decide to just use python, due to things that don't exist in modern langauges and would
require threading to be able to execute properly (though not necessarily in the same way
as it was executed on the older computers)

[The book is now available online to download for free](https://drive.google.com/file/d/0Bxv0SsvibDMTVUExUjFhTURCSU0/view)

## Executing the Games

A *shebang* has been included in the files so that they can be executed directly from the
command line. However, for that to work you will need to make the file executable. Since these
games run only on Linux, you will need to go to the directory on the command line and type

*chmod +x [game name].py*

## Issues

<ins>Get/Inkey</ins>

Basic had two means of getting a user input, the *input* command, which would block the
program from going further until an input (followed by pressing Enter), and it would 
have the prompt '?'

The other means would be either *Get* or *inkey* depending on the computer you were using. This
command would check for a keypress *at a given instance* and if there was one, then it would be recorded.
It would be a means of getting rid of the annoying '?', or as a means of timing the input, except
only one character would be recorded. Normally it would for a loop, and once keypress is detected, it
would escape from the loop.

The main idea is that the *get* or *inkey* would not block the program from executing while waiting
for the user to press a key (or series of keys)

**Update**
[I have found this link](https://stackoverflow.com/questions/60896414/python-preferably-3-equivalent-to-inkey)
I have yet to try it out though.
No, it didn't work as I hoped it would.

**Keyboard**
There is a python package called [keyboard](https://pypi.org/project/keyboard/). This has a number of functions
one of them involving detecting key presses. However, there are a couple of problems:

1) When the key is pressed, it still appears on the screen (it doesn't with Inkey)
2) It will detect specific keys as opposed to general keypresses (though I believe it can detect that)
3) It will detect a key, not a combination of keys (though I looks like that is possible as well)
4) You require root privileges to access the command, otherwise an error will be thrown

I attempted to use it on one of the games, but unfortunately it didn't work as expected.

<ins>Computer Crash</ins>
I had already converted a number of the games across, but since I was using it for practice, silly me
didn't save a copy, or upload it to github. As such, when my laptop failed, the linux partitions on the
harddrive seemed to have been wiped so it looks like they have been lost.

## Games

**Robot Invaders**

This game will flash a character up on the screen, and the player is supposed to reproduce that character
before a time limit is up. As with all of the games, I have added the extra component that they suggest you
do, which is having certain character worth more points than others. I have also added a difficulty
function so the player can set a difficulty level, which means that the time limit is less for higher
difficulties

**Secret Weapon**

This is a simple guessing game. You enter a difficulty that is greater than 3, and based on that difficulty
the computer calculates the location of the target, and how many turns the player has (the higher the difficulty, the more turns). The player then enters co-ordinates, that the computer responds with whether the
player has got close, missed, or hit the target. A score is also recorded, based on how close, and whether the
player has hit. The more times the player gets close, before hitting the target, the higher the score.

**Escape**

This is another guessing game. This one the player has to guess a number that represents the robot's frequency
There are a number of ways the player can die. I have set variables that can be adjusted to change the
frequency though I have not written a difficulty setting function. The player dies if they either run out of
goes, gets a frequecy that is too high (twice) or too low (twice).

**Pirate Dogfight**

This is more of an action/arcade game, where you have to match the speed, and location, of the opponent
and then attempt to shoot them down. If the opponent gets too far away, then you lose. There is also a 50%
chance that the opponent will shoot you instead of you shooting them. However, there is code that can show
the opponent, and yourself, on the screen, which has been incorporated. You speed up/slow down/shoot using
specific keys.

**Supersonic Bomber**

This game requires you to select the correct item within a limited amount of 
time. The player is given a graph, and the player must select the biggest graph
from the list. The game runs for 10 turns, and each turn the time gets shorter
and shorter. I have included a difficulty selection for the game, so that the
higher the difficulty, the more selections the player has, and the shorter
the time the player has to select them.

**Iceberg**

This game prints out an 8x8 grid with an enemy ship and icebergs. The goal of the game is to attempt to
get the enemy ship to crash into an iceberg. The AI is really primitive (considering that it is a game for
some old 80s computers) in that it justs moves directly towards you (though I'm sure you could make it a
little harder). I have basically written it as is, though I have made the text a little better, and used
slightly different symbols, though they are all character based. Mind you, the game is quite difficult
nonetheless. I have also added quit, and stand still options as well.

**Wizard's Wall**

This was a rather tricky game to translate since there are a lot of mathematical equations that are used to
determine whether the player has won or not. In fact, I'm still not quite sure whether I have managed to get
all of the equations working. The second thing is that the original listing doesn't have any comments so I
can't go through and determine whether I have completed it correctly. Sure, the game runs, but I'm not quite
sure whether it runs the way it is supposed to. Further, the basic code is pretty horrid to follow.

The idea is to knock down a wall, and you do that by selecting an angle and a speed. The wall can move at
times, and if it moves too much, well, you die. The instructions are included in the game, and you also
have a difficulty level too. However, translating this game reminds me of how much simpler modern languages
are as opposed to the ones from my childhood.

