# MorseCodeTranslator
 Translate english into  morse code  

Abstract:

We can use python or any other programming language to execute this program. So, we are using python here to convert English into Morse code using concepts of python like dictionaries, for loop, etc. We are asking a user to input a string in English. After that we are storing the string in an empty string container. Then applying a for loop to contain an English letter into Morse code. Then creating dictionary which will hold all the alphabets: Morse letters key: value pairs. As we are creating a function which will return the value of Morse code.

Introduction:

What is a Morse code?
The Morse code is a method of sending text messages by keying in a series of electronic pulses, usually represented as a short pulse (called a 'dot') and a long pulse (a 'dash').

Is Morse code used today?
Yes!! Morse Code is most prevalent in Aviation and Aeronautical fields since radio navigational aids such as VOR and NDB still identify in Morse Code. The US Navy and Coast Guard still use signal lamps to communicate via Morse Code.

Where Morse code was used?
The purpose of the telegraph was to provide rapid communication of long distances. The method of communication used in the telegraph was Morse Code, which was a series of dots and dashes made up of electric currents being alternated.

Algorithm:

Step 1: Create a function with parameter ‘text’ and do up to  Step 4.

Step 2: Create a dictionary holding key value pairs of Morse code.

Step 3: Create an empty string to hold the alphabets.

Step 4: Apply a for loop with x in text
    Empty string += dictionary(x.lower())
    Return string.
    
Step 5: Input text from a user.

Step 6: Print function(text).

Step 7: End.
