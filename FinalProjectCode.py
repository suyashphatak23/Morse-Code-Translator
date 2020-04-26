'''

Morse Code Translator
@author : Suyash Shivaji Phatak
Date: 15/11/2019

'''

# Dictonary for morse code and alphabets
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ', ':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-'
}

# Function for converting string into morse-code

def morsify(text):
   morse_code = ''
   for x in text:
      if x != ' ':
         morse_code += MORSE_CODE_DICT[x] + ' '
      else:
         morse_code += ' '
   return morse_code

# Main function

def main():
   my_text = input("\nEnter a string in English to convert in Morse code: ")
   output = morsify(my_text.upper())
   print ('\nYour Morse code is ' + output)

if __name__ == '__main__':
   main()
