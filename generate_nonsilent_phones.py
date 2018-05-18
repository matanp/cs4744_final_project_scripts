
##look at lexicon file and generate a list of all the phones

if __name__ == "__main__":
	with open("lexicon.txt", "r") as f:
		lexicon = f.read()

	lines = lexicon.split("\n")

	phones = []

	for i in range(5,len(lines) -1):
		pronounce = lines[i-1].split("\t")[1]
		pronounce = pronounce.split(" ")
		for phone in pronounce:
			if phone in phones:
				continue
			else:
				phones.append(phone)

		
	with open("nonsilence_phones.txt", "w") as f:
		for phone in sorted(phones):
			f.write(phone + "\n")			


		
