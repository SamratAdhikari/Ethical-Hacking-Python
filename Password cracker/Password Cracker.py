# Password Cracker

import hashlib, pyperclip


def main():
	myPass = str(input("Enter the password/passhash: "))
	pass_mode = str(input("[E]ncrypt or [D]ecrypt: "))

	if pass_mode.upper().startswith("E"):
		encryptHash(myPass)
	elif pass_mode.upper().startswith("D"):
		decryptHash(myPass)
	else:
		print("Invalid Input...")


def encryptHash(msg):
	pass_hash = hashlib.md5(str.encode(msg)).hexdigest()

	with open("wordlist.txt", "a") as f:
		f.write("\n" + msg.strip())

	print("\nEncrypted Password is: " + pass_hash)
	print("Copied the PassHash to the clipboard")
	pyperclip.copy(pass_hash)


def decryptHash(msg):
	pass_file = open("wordlist.txt", "r")
	flag = 0

	for word in pass_file:
		encode_word = word.encode("utf-8")
		digest = hashlib.md5(encode_word.strip()).hexdigest()

		if digest == msg:
			print("Password has been found !\nPassword : " + word)
			# return "Password has been found !\nPassword : " + word
			flag = 1
			print("Copied the PassWord to the clipboard")
			pyperclip.copy(word)
			break

	if flag == 0:
		print("\nPassword/Passphase is not in the list...")
		ask = input("\nDo you know the Decrypted Password?(y/n) ")
		if ask == "y":
			ask_pass = input("Type the Password: ")
			with open("wordlist.txt", "a") as f:
				f.write(ask_pass.strip())


if __name__ == '__main__':
	run = True
	while run:
		main()
		play = input("\nRun the Program again?(y/n) ")
		if play != "y":
			run = False
