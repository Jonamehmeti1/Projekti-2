from encode import encode
from decode import decode1
from sound import play_morse
from morse_dict import MORSE_CODE, DECODE_MORSE

choice = input("Shkruaj 'enkriptim' ose 'dekriptim': ")

if choice.lower() == "enkriptim":

    while True:
        text = input("Shkruaj tekstin (ose 'exit' për me dal): ")

        if text.lower() == "exit":
            break

        morse = encode(text)
        print("Morse Code:", morse)

        play_morse(morse)

        print("Decoded:", decode1(morse))
        print("\n---\n")

elif choice.lower() == "dekriptim":

    while True:
        morse_input = input("Shkruaj Morse code (ose 'exit' për me dal): ")

        if morse_input.lower() == "exit":
            break

        play_morse(morse_input)

        print("Dekodu:", decode1(morse_input))
        print("\n---\n")

else:
    print("Opsion i pavlefshëm.")
