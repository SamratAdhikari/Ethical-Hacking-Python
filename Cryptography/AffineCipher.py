# AffineCipher

import sys, pyperclip, random
import CryptoMath

Symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
# print(len(Symbols) ** 2)


def main():
	myMsg = str(input("Enter your Message:\n"))
	myKey = int(input("\nEnter your Key: "))
	myMode = str(input("\n[E]ncrypt or [D]ecrypt: "))

	if myMode.upper().startswith("E"):
		translated = encryptMessage(myKey, myMsg)
		print("\nEncrypting...\n")

	elif myMode.upper().startswith("D"):
		translated = decryptMessage(myKey, myMsg)
		print("\nDecrypting...\n")

	print(f"Key: #{myKey}")
	print(translated)
	print("\nCopied the translated text to clipboard")
	pyperclip.copy(translated)


def getKeyParts(key):
	keyA = key // len(Symbols)
	keyB = key % len(Symbols)
	return keyA, keyB


def checkKeys(keyA, keyB, mode):
	if keyA == 1 and mode == "encrypt":
		sys.exit("\nCipher is Weak if the KeyA is 1. Choose a different key.")

	if keyB == 0 and mode == "encrypt":
		sys.exit("\nCipher is Weak if the KeyB is 1. Choose a different key.")

	if keyA < 0 or keyB < 0 or keyB > len(Symbols)-1:
		sys.exit("\nKeyA must be greater 0 and KeyB must be between 0 & " + str(len(Symbols)-1))

	if CryptoMath.gcd(keyA, len(Symbols)) != 1:
		sys.exit(f"Key A {keyA} and symbol set size {len(Symbols)} are not relatively prime. Choose a different key.")


def encryptMessage(key, message):
	keyA, keyB = getKeyParts(key)
	checkKeys(keyA, keyB, "encrypt")
	cipherText = ""

	for symbol in message:
		if symbol in Symbols:
			# Encrypt the symbol
			symbolIndex = Symbols.find(symbol)
			cipherText += Symbols[(symbolIndex * keyA + keyB) % len(Symbols)]
		else:
			cipherText += symbol

	return cipherText


def decryptMessage(key, message):
	keyA, keyB = getKeyParts(key)
	checkKeys(keyA, keyB, "decrypt")
	plainText = ""
	modInverseOfKeyA = CryptoMath.findModInverse(keyA, len(Symbols))

	for symbol in message:
		if symbol in Symbols:
			# Decrypt the symbol
			symbolIndex = Symbols.find(symbol)
			plainText += Symbols[(symbolIndex - keyB) * modInverseOfKeyA % len(Symbols)]
		else:
			plainText += symbol

	return plainText


def getRandomKey():
	while True:
		keyA = random.randint(2, len(Symbols))
		keyB = random.randint(2, len(Symbols))

		if CryptoMath.gcd(keyA, len(Symbols)) == 1:
			return keyA * len(Symbols) + keyB


if __name__ == '__main__':
	main()


















