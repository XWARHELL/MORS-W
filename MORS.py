
# Create the logo
logo = pyfiglet.figlet_format("WarHell")

# Color the logo
colored_logo = colored(logo, color="Yellow")

# Print the logo
print(colored_logo)


colored_text = colored("\n  -- (WarHell) -- [Professional Warhill Morse Code Translator Follow us on GitHub]\n  -- (WarHell) -- [ github : https://gthub.com/XWARHELL ]", "blue")

# Print the colored text
print(colored_text)
print("")
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
                   'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
                   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
                   'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
                   'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
                   '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', 
                   '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'}

def translate_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += char + ' '
    return morse_code

def translate_to_text(morse_code):
    text = ''
    for code in morse_code.split():
        for char, morse in MORSE_CODE_DICT.items():
            if morse == code:
                text += char
        else:
            text += ' '
    return text

def translate_morse():
    while True:
        word = input(" What word should I translate? ")
        if word[0] == '.' or word[0] == '-':
            answer = translate_to_text(word)
            print("MORS:", answer)
        else:
            answer = translate_to_morse(word)
            print("MORS:", answer)

translate_morse()
