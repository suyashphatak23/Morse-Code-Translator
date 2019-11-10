#BY SUYASH PHATAK

#Python File

#MORSE CODE TRANSLATOR

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
def morsify(text):
   morse_code = ''
   for x in text:
      if x != ' ':
         morse_code += MORSE_CODE_DICT[x] + ' '
      else:
         morse_code += ' '
   return morse_code
def main():
   my_text = input("Enter a string in English to convert in Morse code:")
   output = morsify(my_text.upper())
   print ('Your Morse code is ' + output)

if __name__ == '__main__':
   main()
