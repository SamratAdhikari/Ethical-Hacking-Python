# Transposition File Cipher

import time, os, sys
import TranspositionEncryption, TranspositionDecryption


def main():
    # inputFileName = 'frankenstein.txt'
    inputFileName = str(input("Enter the input file name: "))
    # BE CAREFUL! If a file with the output file name already exists,
    # this program will overwrite that file:
    outputFileName = str(input("Enter the output file name: "))
    # outputFileName = 'frankenstein.output.txt'

    myMode = str(input("[E]ncrypt or [D]ecrypt: "))
    myKey = int(input("Enter the Key: "))

    # If the input file doesnt exists, the program terminates
    if not os.path.exists(inputFileName):
        print(f"The file {inputFileName} doesnt exist!\nExiting the program...")
        sys.exit()

    # If the output file already exists, give the user a chance to quit
    if os.path.exists(outputFileName):
        ask = input(f"Overwrite the file {outputFileName}\n[C]ontinue or [Q]uit? ")

        if not ask.lower().startswith("c"):
            sys.exit()


    # Read the input file 
    fileObj = open(inputFileName)
    content = fileObj.read()
    fileObj.close()

    # Measure how long the encryption/decrypting takes place
    startTime = time.time()

    if myMode.lower().startswith('e'):
        print("\nEncrypting...\n")
        translated = TranspositionEncryption.encryptMessage(myKey, content)

    elif myMode.lower().startswith('d'):
        print("\nDecrypting...\n")
        translated = TranspositionDecryption.decryptMessage(myKey, content)

    totalTime = round(time.time() - startTime, 2)
    print("Time taken: " + str(totalTime))

    # Write out the translated message to output file
    outputFileObj = open(outputFileName, "w")
    outputFileObj.write(translated)
    outputFileObj.close()

    print(f'Done, Total {len(content)} characters.')
    print(f'Output File: {outputFileName}')


if __name__ == '__main__':
    main()
















































