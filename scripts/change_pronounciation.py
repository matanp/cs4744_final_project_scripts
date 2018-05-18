

if __name__ == "__main__":

	## tuples of english pronounce, spanish pronounce
	changes = [("A", "B"), ("E", "F")]

	with open("../cmu_pronounciation", "r") as f:
		text = f.read()
		text = text.replace("\t", " ")
		lines = text.split("\n")
		new_text = ""
		for line in lines:
			word = line.split(" ")[0]	
			pronounce = " ".join(line.split(" ")[1:])
			new_pronounce = pronounce
			for change in changes:
				new_pronounce = new_pronounce.replace(change[0], change[1])
			
			new_line = word + "\t" + new_pronounce

			new_text = new_text + new_line + "\n"

	with open("spanish_cmu_pronounciation", "w") as f:
		f.write(new_text)
			
