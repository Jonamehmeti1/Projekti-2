
from morse_dict import MORSE_CODE

def encode(text):
    text = text.upper()
    result = []

    for c in text:
        if c in MORSE_CODE:
            result.append(MORSE_CODE[c])

    return ' '.join(result)