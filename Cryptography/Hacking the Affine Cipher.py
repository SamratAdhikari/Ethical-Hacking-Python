# Hacking the Alphine Cipher

import pyperclip
import CryptoMath, AffineCipher, DetectEnglish

SILENT_MODE = False
Symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def main():
	# myMsg = """5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu"""
	myMsg = str(input("Enter the Cipher Text: "))

	hacked = hackAffine(myMsg)

	if hacked != None:
		print()
		print(hacked)
		print("\nCopied Hacked Message to Clipboard")
		pyperclip.copy(hacked)

	else:
		print("Failed to hack the encryption")


def hackAffine(message):
	print("\nPress Ctrl + C to quit at any time")

	# Brute force by looping through every possible key
	for key in range(len(Symbols) ** 2):
		keyA = AffineCipher.getKeyParts(key)[0]
		if CryptoMath.gcd(keyA, len(AffineCipher.Symbols)) != 1:
			continue

		decryptedText = AffineCipher.decryptMessage(key, message)

		if not SILENT_MODE:
			print(f"Try Key #{key}...")

		if DetectEnglish.isEnglish(decryptedText):
			# Check with the user if the decrypted key has been found
			print("\nPossible Encryption Hack:")
			print(f"#{key} | Decrypted Message:\n")
			print(decryptedText[:200])

			ask = input("\nEnter D for done or Press Enter to Continue Hacking: ")
			if ask.strip().upper().startswith("D"):
				return decryptedText

	return None


if __name__ == '__main__':
	main()





























