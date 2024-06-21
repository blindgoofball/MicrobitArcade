from microbit import *
import speech
import beepybird
import tiltattack

games={
    'Beepy Bird':beepybird,
    'Tilt Attack':tiltattack
}

speech.say('Welcome to the Microbit arcade!')
speech.say('Select a game with the a and b buttons, and touch the logo to start.')
selection=-1
while True:
    if button_b.was_pressed():
        selection=selection+1 if selection+1 < len(games) else 0
        speech.say(list(games)[selection])
    if button_a.was_pressed():
        selection=selection-1 if selection-1 >= 0 else len(games)-1
        speech.say(list(games)[selection])
    if pin_logo.is_touched() and selection != -1:
        break
list(games.values())[selection].main()
reset()