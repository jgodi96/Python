Alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Key = 3

#encryption algorithm
def caesar_encrypt(plain_text):
	#encrypt message
	cipher_text=''
	#make the algorithm case insensitive
	plain_text=plain_text.upper();

	for c in plain_text:
		#numerical representation
		index=Alphabet.find(c)
		#arithmetic equation
		index=(index+Key)%len(Alphabet)
		#appending
		cipher_text = cipher_text + Alphabet[index]
	return cipher_text
#decryptionalgorithm
def caesar_decrypt(cipher_text):
	plain_text = ''
	for c in cipher_text:
		index=Alphabet.find(c)
		index=(index-Key)%len(Alphabet)
		plain_text=plain_text+Alphabet[index]

	return plain_text

if __name__=="__main__":
	encrypted = caesar_encrypt('This is an example')
	print(encrypted)
	decrypted = caesar_decrypt(encrypted)
	print(decrypted)
