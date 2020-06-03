import matplotlib.pylab as plt

LETTERS=' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def frequency_analysis(plain_text):
	plain_text=plain_text.upper()
	#using dictionary pair
	letter_frequency = {}

	for letter in LETTERS:
		letter_frequency[letter]=0

	for letter in plain_text:
		if letter in LETTERS:
			letter_frequency[letter]+=1
	return letter_frequency
def plot_distr(letter_frequency):
	centers = range(len(LETTERS))
	plt.bar(centers,letter_frequency.values(), align='center',tick_label=letter_frequency.keys())
	plt.xlim([0,len(LETTERS)-1])
	plt.show()

if __name__ == "__main__":
	plain_text = "Shannon defined the quantity of information produced by a source, for example the quantity"
	frequencies = frequency_analysis(plain_text)
	plot_distr(frequencies)
