# Transposition Cipher Decryption

import math, pyperclip


def main():
    myMsg = str(input("Enter the encrypted code: "))
    myKey = int(input("Enter the key: "))

    plainText = decryptMessage(myKey, myMsg)

    # Print with a | (called "pipe" character) after it in case
    # there are spaces at the end of the decrypted message:
    print(plainText + "|")

    pyperclip.copy(plainText)


def decryptMessage(key, msg):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.

    # The number of "columns" in our transposition grid:
    Cols = int(math.ceil(len(msg) / float(key)))

    # The number of rows in our grid
    Rows = key

    # The number of shaded boxes in the last column
    Shade = (Cols * Rows) - len(msg) 

    # Each string in plaintext represents a column in the grid:
    plainText = [""]*Cols

    # The column and row variables point to where in the grid the next
    # character in the encrypted message will go:
    column = 0
    row = 0
   
    for symbol in msg:
        plainText[column] += symbol
        column += 1 # Point to the next column.
   
        # If there are no more columns OR we're at a shaded box, go back
        # to the first column and the next row:
        if (column == Cols) or (column == Cols - 1 and row >= Rows - Shade):
            column = 0
            row += 1
   
    return ''.join(plainText)
   

# If transpositionDecrypt.py is run (instead of imported as a module),
# call the main() function:
if __name__ == "__main__":
    main()










