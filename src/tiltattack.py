from microbit import *
import music
import speech
from random import randint

def main():
    tiltDistance=400
    target=randint(2, 48)
    position=25
    score=0
    for _ in range(3):
        music.pitch(440, 100)
        sleep(1000)
    music.pitch(880, 500)
    while True:
        if accelerometer.get_x() < -tiltDistance:
            position=max(0, position-1)
        elif accelerometer.get_x() > tiltDistance:
            position=min(position+2, 50)
        if target-2 <= position <= target+2:
            music.pitch(440, 10)
        if button_a.was_pressed() and target-2 <= position <= target+2:
            music.pitch(1000, 100)
            target=randint(2, 48)
            score+=1
        if running_time() >= 60000:
            break
        sleep(50)
    for _ in range(5):
        music.pitch(100, 50)
    speech.say('Your score is: '+str(score))

if __name__ == '__main__':
    main()