from microbit import *
import speech
import music
from random import randint

position=[0, 100]
target=randint(50, 300)
score=0
for _ in range(3):
    music.pitch(440, 200)
    sleep(1000)
music.pitch(880, 400)
while True:
    position[0]+=1
    if  button_a.is_pressed():
        position[1]+=10
    else:
        position[1]=max(0, position[1]-10)
    if position[1] < target-25:
        music.pitch(200, 10)
    elif position[1] > target+25:
        music.pitch(500, 10)
    if position[0] >= 50:
        if position[1] < target-20 or position[1] > target+20:
            break
        target=randint(50, 300)
        music.pitch(1000, 100)
        score+=1
        position[0]=0
    sleep(100)
music.pitch(100, 500)
speech.say('Your score is: '+str(score))