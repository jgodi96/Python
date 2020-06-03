Alphabet = ' ABCDEFGHJKLMNOPQRSTUVWXYZ'
def caesar_crack(cipher_text):
	for key in range (len(Alphabet)):
		plain_text = ''

		for c in cipher_text:
			index = Alphabet.find(c)
			index = (index-key)%len(Alphabet)
			plain_text = plain_text + Alphabet[index]

		print('With key %s, the result is: %s'%(key,plain_text))
if __name__=="__main__":
	encrypted = 'VJKUBKUBCBOGUUCIG'
	caesar_crack(encrypted)

