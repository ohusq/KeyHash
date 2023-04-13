import secrets
import codecs

def Rot13(string, amount):
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

CurrentRot = secrets.randbelow(26) + 1

def Encrypt():

	print("Encrypting")
	global mainKey
	mainKey = Rot13("actualKey", CurrentRot)
	key = secrets.token_hex(16)
	
	# Key algorithm
	global newKey
	global randomInt

	randomInt = secrets.randbelow(16) + 1
	newKey = (key[0:randomInt] + mainKey + key[randomInt:32])

	print("Key: " + newKey)
	
	print("Encrypted")

def Decrypt():
	print("Decrypting")

	# Key algorithm
	global newKey
	global randomInt
	# Decode key
	key = newKey[ randomInt : randomInt + len(mainKey) ]
	key = Rot13(key, -CurrentRot)

	
	print("Key: " + key)
	
	print("Decrypted")

print("Starting")
Encrypt()
print("Done Encrypting\n\n")
Decrypt()
print("Done Decrypting")