# Morse Code

from playsound import playsound
import time
import pyttsx3 as pyttsx
import pyperclip

MORSE_CODE = {
    ' ':'/', 
    'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 
    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 
    'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.','O':'---', 
    'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', 
    '6':'-....','7':'--...', '8':'---..', '9':'----.', '0':'-----', 
    ', ':'--..--', 
    '.':'.-.-.-',
    '?':'..--..', 
    '/':'-..-.', 
    '-':'-....-',
    '(':'-.--.', 
    ')':'-.--.-',
}


def Txt_Morse(Text):
    plainTxt = Text
    code = [MORSE_CODE[i.upper()] + ' ' for i in plainTxt if i.upper() in MORSE_CODE.keys()]
    morse = ''.join(code)

    # return "\n" + morse + "\nMessage copied to clipboard..."
    print("\n" + morse)
    pyperclip.copy(morse)

    for m in morse:
        if  m == ".":
            playsound('dot.wav')
        elif m == "-":
            playsound('dash.wav')
        else:
            time.sleep(0.5)

    print("Message copied to clipboard") 


def Morse_Txt(Text):
    morse = Text
    code = [k for i in morse.split() for k, v in MORSE_CODE.items() if i == v]
    plainTxt = ''.join(code)

    pyperclip.copy(plainTxt)
    print("\n" + plainTxt) 

    engine = pyttsx.init()
    engine.say(plainTxt)
    engine.runAndWait()

    print("Message copied to clipboard") 

def main():
    while True:
        try:
            myMsg = str(input("\n\nEnter the Message:\n"))
            ask = int(input("\nEnter your choice...\nText to Morse[1] or Morse to Text[2]\nQuit[3]:\n"))

            if ask == 1:
                Txt_Morse(myMsg)

            elif ask == 2:
                Morse_Txt(myMsg)

            elif ask == 3:
                break

        except:
            print("Something went wrong! PLease try again...")


if __name__ == '__main__':
    main()
    
