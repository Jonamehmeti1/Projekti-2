import winsound
import time

def play_morse(morse):
    frequency = 800
    dot_duration = 150
    dash_duration = 450

    for symbol in morse:
        if symbol == '.':
            winsound.Beep(frequency, dot_duration)
        
        

