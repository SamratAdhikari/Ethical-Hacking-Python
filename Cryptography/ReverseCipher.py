# Reverse Cipher


def main():
	msg = str(input("Enter your message: "))
	ask = str(input("Encrypt[E] or Decrypt[D]: "))

	if ask.upper() == "E":
		msg = msg[::-1]

	elif ask.upper() == "D":
		msg = msg[::-1]

	else:
		print("Invalid Input")

	print(msg)

if __name__ == "__main__":
	main()