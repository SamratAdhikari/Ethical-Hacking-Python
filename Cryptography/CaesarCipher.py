# Caesar Cipher

import pyperclip


def main():
	# Msg to encode or decode
	msg = str(input("Enter your message: "))

	# whether program encrypts or decrypts
	mode = str(input("Encrypt[E] or Decrypt[D]: ")).upper() # Set to either "encrypt" or "decrypt"

	# Encrypt/Decrypt Key
	key = int(input("Enter the Cipher Key: "))

	# Symbols
	SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,<>!$%&#@?{ }()[]_-^"

	# Store the encrypted/decrypted form of msg
	trans = ""

	for symbol in msg:
		if symbol in SYMBOLS:
			symbolIndex = SYMBOLS.find(symbol)

			# Perform encryption/decryption
			if mode == "E":
				transIndex = (symbolIndex + key) % len(SYMBOLS)

			elif mode == "D":
				transIndex = (symbolIndex - key) % len(SYMBOLS)

			else:
				print("Invalid Input")

			# Set ciphered code
			trans += SYMBOLS[transIndex]

		else:
			# Append the symbol without encryption/decryption
			trans += symbol

	# Output
	print(trans)
	pyperclip.copy(trans)


def run():
	print()
	main()
	print()
	ask = str(input("Run the program again?(y/n) ")).lower()
	if ask == "y":
		run()

run()