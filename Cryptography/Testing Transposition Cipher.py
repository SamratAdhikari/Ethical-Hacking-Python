# Testing Transposition Cipher

import sys, random, TranspositionEncryption, TranspositionDecryption


def main():

	ask = int(input("How many times to run the code? "))
	random.seed(42) # Set the random "seed" to a static value

	for i in range(ask): 
		# Generate random message to test
		# The message will have a random length
		msg = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * random.randint(4, 40)

		# Convert the message string to a list to shuffle it
		msg = list(msg)

		random.shuffle(msg) # Shuffle is used with lists
		msg = ''.join(msg) # Convert the lists back to string

		print(f"Testing #{i+1}: '{msg[0:20]}'")

		# Check all possible keys for each message
		for key in range(1, ask):
			encrypted = TranspositionEncryption.encryptMessage(key, msg)
			decrypted = TranspositionDecryption.decryptMessage(key, encrypted)

			# If the decryption doesnt match the original message, display an error message and quit
			if msg != decrypted:
				print(f"Mismatch with key {key} and message {msg}\n\n")
				print("Decrypted as: " + decrypted)
				sys.exit()

	print("Transposition Cipher Test Passed !")


if __name__ == '__main__':
	main()













