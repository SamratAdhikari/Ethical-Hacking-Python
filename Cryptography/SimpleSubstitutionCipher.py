# Simple Substitution Cipher

import pyperclip, sys, random

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
	myMsg = str(input("Enter your message: "))

	myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
	myMode = str(input("[E]ncrypt or [D]ecrypt: "))

	if not keyInvalid(myKey):
		sys.exit("\nThere is an error in the key or symbol set...")

	if myMode.upper().startswith("E"):
		translated = encryptMessage(myKey, myMsg)

	elif myMode.upper().startswith("D"):
		translated = decryptMessage(myKey, myMsg)

	print("\nUsing key: " + myKey)
	print("The Translated Message is:\n" + translated)
	print("\nMessage has been copied to clipboard.")
	pyperclip.copy(translated)


def keyInvalid(key):
	keyList = list(key)
	letterList = list(LETTERS)
	keyList.sort()
	letterList.sort()
	# print(keyList, letterList)

	return keyList == letterList


def encryptMessage(key, message):
	return translateMessage(key, message, "encrypt")


def decryptMessage(key, message):
	return translateMessage(key, message, "decrypt")


def translateMessage(key, message, mode):
	translated = ''
	charA = LETTERS
	charB = key

	if mode == "decrypt":
		# For decrypting, we can use the same code as encrypting. We
		# just need to swap where the key and LETTERS strings are used.
		charA, charB = charB, charA

	# Loop through each symbol in the message:
	for symbol in message:
		if symbol.upper() in charA:
			# Encrypt/Decrypt the symbol
			symbolIndex = charA.find(symbol.upper())

			if symbol.isupper():
				translated += charB[symbolIndex].upper()
			else:
				translated += charB[symbolIndex].lower()

		else:
			# Symbol is not in LETTERS, just add it
			translated += symbol

	return translated


def getRandomKey():
	key = list(LETTERS)
	random.shuffle(key)
	return ''.join(key)


if __name__ == '__main__':
	main()

