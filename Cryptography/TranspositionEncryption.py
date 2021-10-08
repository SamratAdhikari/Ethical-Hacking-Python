# Transposition Cipher Encryption

import pyperclip


def main():
    myMsg = str(input("Enter the message: "))
    myKey = int(input("Enter the key: "))

    cipherText = encryptMessage(myKey, myMsg)

    """
     Print the encrypted string in ciphertext to the screen,
     with a | ("pipe character") after it in case there are 
     spaces at the end of the encrypted message
     """
    print(cipherText + '|')

     #Copy the encrypted string in ciphertext to clipboard
    pyperclip.copy(cipherText)


def encryptMessage(key, message):
    # Each string in ciphertext represents a column in the grid
    ciphertext = ['']*key

    # Loop through each column in ciphertext
    for column in range(key):
        currentIndex = column

        # Keep looping until currentIndex goes past the message length
        while currentIndex < len(message):
            # Place the character at currentIndex in messageat the end of the current column in the ciphertext list
            ciphertext[column] += message[currentIndex]

            # Move currentIndex over
            currentIndex += key

    # Convert the ciphertext list into a single value and return it
    return ''.join(ciphertext)


# If the file is not imported
if __name__ == '__main__':
    main()





















