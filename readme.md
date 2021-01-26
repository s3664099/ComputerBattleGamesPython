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