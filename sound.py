import winsound
import time

def play_morse(morse):
    frequency = 800
    dot_duration = 150
    dash_duration = 450

    for symbol in morse:
        if symbol == '.':
            winsound.Beep(frequency, dot_duration)
        elif symbol == '-':
            winsound.Beep(frequency, dash_duration)
        elif symbol == ' ':
            time.sleep(0.2)
        elif symbol == '/':
            time.sleep(0.6)

  


