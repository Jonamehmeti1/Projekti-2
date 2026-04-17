from morse_dict import DECODE_MORSE

def decode1(morse):
    words = morse.split(' ')
    decoded_text = ""

    for w in words:
        if w == '/':
            decoded_text += " "
        elif w in DECODE_MORSE:
            decoded_text += DECODE_MORSE[w]
        else:
            decoded_text += '?'
    
    return decoded_text