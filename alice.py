# A small program that outputs the number of words in a given program

def count_words(filename):
	'''Count the approximate number of words in the file.'''

	try:
		with open(filename, encoding='utf-8') as f_obj:
			contents = f_obj.read()

	except FileNotFoundError: 
		msg = 'Sorry, the file ' + filename + ' does not exsist.'
		print(msg)

	else: 
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about, " + str(num_words) + " words.")

filename = 'alice.txt'
count_words(filename)  