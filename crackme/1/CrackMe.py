import secrets
import tkinter as tk

def rot13(string, amount):
	output = ""
	for i in string:
		if i.isalpha():
			num = ord(i)
			num += amount

			if i.isupper():
				if num > ord("Z"):
					num -= 26
				elif num < ord("A"):
					num += 26
			elif i.islower():
				if num > ord("z"):
					num -= 26
				elif num < ord("a"):
					num += 26

			output += chr(num)
		else:
			output += i
	return output

class Encryption:
	def __init__(self, secret_key):
		self.secret_key = secret_key

	def encrypt(self, plaintext):
		ciphertext = ""
		for i in plaintext:
			ciphertext += rot13(i, self.secret_key)
		return ciphertext

	def decrypt(self, ciphertext):
		plaintext = ""
		for i in ciphertext:
			plaintext += rot13(i, -self.secret_key)
		return plaintext

class App:
	def __init__(self, master):
		self.master = master
		self.frame = tk.Frame(self.master)
		self.master.geometry("300x200")
		self.frame.pack()

		self.input = tk.Entry(self.frame)
		self.input.pack()

		self.auth_button = tk.Button(self.frame, text="Auth", command=self.authenticate)
		self.auth_button.pack()

		self.quit_button = tk.Button(self.frame, text="Quit", command=self.frame.quit)
		self.quit_button.pack()

		self.encryption = Encryption(secrets.randbelow(26) + 1)
		self.actual_key = self.encryption.encrypt("heheheha")

	def authenticate(self):
		user_input = self.input.get()
		encrypted_input = self.encryption.encrypt(user_input)
		if encrypted_input == self.actual_key:
			print("Authenticated")
		else:
			print("Incorrect")

root = tk.Tk()
app = App(root)
root.mainloop()
