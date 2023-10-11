# text-based (command line) program that takes any String input and converts it into Morse Code.
string_input = input('Enter text: ')

# morse code dictionary representation.
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '}

morse_code = []
new_code = ''
for letter in string_input:
    for morse in morse_code_dict:
        if letter.lower() == morse.lower():
            morse_code.append(morse_code_dict[morse])
            new_code = ' '.join(morse_code)

print(morse_code)
print(new_code)
