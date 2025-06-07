import winsound
import time

MORSE_CODE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.', 
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',  ' ': '/'
}

DOT_DURATION = 150   # milliseconds
DASH_DURATION = 450  # milliseconds
FREQ = 800           # Hz

def play_morse(text):
    for char in text.upper():
        if char not in MORSE_CODE_DICT:
            continue
        code = MORSE_CODE_DICT[char]
        for symbol in code:
            if symbol == '.':
                winsound.Beep(FREQ, DOT_DURATION)
            elif symbol == '-':
                winsound.Beep(FREQ, DASH_DURATION)
            time.sleep(0.1)
        time.sleep(0.3)  # space between letters
    print("Finished playing Morse code.")

user_input = input("Enter text to convert to Morse Code and play: ")
play_morse(user_input)
