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

To execute the game *Missile!*, PyGame needs to be installed.

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

**Pygame**
This is also a solution, but it adds a lot more to the game than otherwise, and adds a lot of time to coding these
games.

<ins>Computer Crash</ins>
I had already converted a number of the games across, but since I was using it for practice, silly me
didn't save a copy, or upload it to github. As such, when my laptop failed, the linux partitions on the
harddrive seemed to have been wiped so it looks like they have been lost.

## Games

**Robot Missile**
This game generates a random number that equates to a letter of the alphabet. The player then must guess
the letter, and if the guess is incorrect, the game will check where the guess is in relation to the letter
and provide a hint.

**Vital Message**
This is a game that tests your memory. A phrase consisting of random letters is displayed for a period of time
and then removed. The player is then required to remember and type the phrase down. If it is correct, the player wins
otherwise the player loses.

**Robot Invaders**

This game will flash a character up on the screen, and the player is supposed to reproduce that character
before a time limit is up. As with all of the games, I have added the extra component that they suggest you
do, which is having certain character worth more points than others. I have also added a difficulty
function so the player can set a difficulty level, which means that the time limit is less for higher
difficulties

**Shoot Out**

This is basically a cow-boy game where you have to shoot before your opponent. You can't shoot until a certain time
and then a timer is given for you to shoot. If you wait too long, you die, otherwise you shoot your opponent. However,
further code has been added so that there is no guarantee that you, or your opponent, will hit you.

**Desert Tank Battle**

This game requires you to guess the location of the enemy. You enter a direction, between -90 and 90, and an elevation
between 0 and 90. If you hit, you hit, however if you miss, a calculation is made as to the position, and a clue as to
where the enemy is located is provided. Also, the enemy has a chance to shoot back at you, and the more you fire (you
have 5 attempts) the more likely that the enemy will spot you and shoot.

**Battle at Traitors Castle**

This game involves an 'archer' appearing on the wall and the player needs to select the correct number between 0 and 9
which corresponds with the archer's position. The play needs to type that number within five seconds otherwise the
shot will be missed (as will the case if the wrong number is typed). A special archer will appear 10% of the time which
will result in a greater score if hit.

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

**Missile!**

I ended up using the PyGame library to create this game, namely because the code that was provided utilises
the various computer's graphics (meaning that there is a separate listing for each of the machines - though
the Commodore 64 isn't among them). The game is simple in that there is a jet that flies across the screen and
you have three missiles which you need to use to shoot it down. If you hit the plane, you win, otherwise you
you lose.

It took me a bit to work it out, and I found that typing it out in the emulators that I found on the internet
didn't seem to produce any working version (and I have to admit that typing games out on one of the 8-bit
machines is so much more problematic than it is writing it on a modern computer, even using something like
vim).

Once I worked out how to use PyGame, creating this game, and even using proper icons, ended up being quite
easy. In fact, I might go back and rewrite some of the games using PyGame - particularly since the Inkey
problem doesn't exist there.

For this game to work, you need to install PyGame, which can be done as follows:

*pip3 install PyGame*

##Updates
**5 October 2022**
Added a file that allows the player to select the game, and also returns the player to that game. Added instructions
to *Robot Invaders*.

**6 October 2022**
Added a play again function to utilities. Fixed up *Robot Invaders*. Fixed up *Secret Weapon* and added instructions.
Fixed up *Escape* and *Pirate Dogfight*. Added a couple more functions to util which are being reused across the games

**15 October 2022**
Added the rest of the games that were rescued from the crash, and converted *Robot Missile*.

**26 October 2022**
Converted *Desert Tank Battle* as well as previous games. Also moved some of the common functions into the util file.

**29 October 2022**
Fixed up issues with *Desert Tank Battle* and added further function where your opponent shoots back. Added *Battle at
Traitor's Castle* which finishes all of the games for this one