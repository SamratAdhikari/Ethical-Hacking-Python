# Vigenere Cipher

import pyperclip

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
	# myMsg = 'Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist.'
	myMsg = str(input("Enter your message:\n"))
	myKey = str(input("Enter the string key: "))
	myMode = str(input("\n[E]ncrypt or [D]ecrypt: "))

	if myMode.upper() == "E":
		translated = encryptMessage(myKey, myMsg)
		print("\nEncrypted Message:\n")

	elif myMode.upper() == "D":
		translated = decryptMessage(myKey, myMsg)
		print("\nDecrypted Message:\n")
	print(translated)
	pyperclip.copy(translated)
	print("\nThe Message has been copied to Clipboard...")


def encryptMessage(key, msg):
	return translateMessage(key, msg, "encrypt")


def decryptMessage(key, msg):
	return translateMessage(key, msg, "decrypt")


def translateMessage(key, msg, mode):
	translated = []

	keyIndex = 0
	key = key.upper()

	for symbol in msg:
		num = LETTERS.find(symbol.upper())

		if num != -1: # -1 means symbol.upper() was not found in LETTERS
			if mode == "encrypt":
				num += LETTERS.find(key[keyIndex]) # Add if encrypting

			elif mode == "decrypt":
				num -= LETTERS.find(key[keyIndex]) # Sub if encrypting

			num %= len(LETTERS) # Handle any wraparound

			# Add the encrypted/decrypted symbol to the end of translated:
			if symbol.isupper():
				translated.append(LETTERS[num])

			elif symbol.islower():
				translated.append(LETTERS[num].lower())

			keyIndex += 1 # Move to next letter in the key

			if keyIndex == len(key):
				keyIndex = 0

		else:
			# Append symbol without translating
			translated.append(symbol)

	return ''.join(translated)


if __name__ == '__main__':
	main()
















