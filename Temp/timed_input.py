import keyboard  # using module keyboard
import time

time_end = time.time() + 12

while time.time() < time_end:  # making a loop

    if keyboard.is_pressed('q'):  # if key 'q' is pressed 
        print('You Pressed A Key!')
        break  # finishing the loop
    #print(time.time())

print("Too Late")
