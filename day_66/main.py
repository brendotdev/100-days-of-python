from tkinter import *

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
    '9': '----.',  ' ': '/',      '.': '.-.-.-',
    ',': '--..--', '?': '..--..', '!': '-.-.--'
}

def to_morse_code():
    user_text = text_entry.get().upper()
    morse = ' '.join(MORSE_CODE_DICT.get(char, '?') for char in user_text)
    output_label.config(text=morse)

# ---------------- UI SETUP ---------------- #
window = Tk()
window.title("Text to Morse Code")
window.config(padx=30, pady=30)

title = Label(text="Morse Code Translator", font=("Arial", 18, "bold"))
title.pack()

text_entry = Entry(width=50)
text_entry.pack(pady=10)
text_entry.focus()

translate_btn = Button(text="Translate", command=to_morse_code)
translate_btn.pack(pady=5)

output_label = Label(text="", font=("Courier", 14), wraplength=400, justify="left")
output_label.pack(pady=10)

window.mainloop()
