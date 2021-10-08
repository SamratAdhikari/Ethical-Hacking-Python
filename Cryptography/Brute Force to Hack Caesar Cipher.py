# Brute Force to Hack Caeser Cipher

msg = str(input("Enter the Message to Decrypt: "))
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,<>!$%&#@?{ }()[]_-^"

# Loop through every possible key
for key in range(len(SYMBOLS)):
	# It is important to set translated to the blank string so that the
	# previous iteration's value for translated is cleared:
	trans = ""

	# rest of the code is almost as same as Caesar Cipher
	# Loop through each symbol in msg
	for symbol in msg:
		if symbol in SYMBOLS:
			symbolIndex = SYMBOLS.find(symbol)
			transIndex = symbolIndex - key

			# Handle the wraparound
			if transIndex < 0:
				transIndex += len(SYMBOLS)

			# Append the decrypted symbol
			trans += SYMBOLS[transIndex]

		else:
			# Append the symbol without encrypting/decrypting
			trans += symbol

	# Display every possible decryption
	print(f"Key {key} : {trans}")





