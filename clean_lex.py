
## make sure all lines in lexicon have a tab before the pronounciation

if __name__ == "__main__":

	with open("lexicon.old.txt", "r") as f:
		lex = f.read()


	lines = lex.split("\n")
	new_lines = []
	count = 0
	for line in lines:
		if "\t" in line:
			print("---")
			print(line)
			print(line.replace(" ","\t", 1))

			new_lines.append(line)
		else:
			print("###")
			print(line)
			print(line.replace(" ","\t", 1))
			new_lines.append(line.replace(" ", "\t", 1))
		count = count + 1
		if count > 50:
			break
	new_lex = "\n".join(new_lines)

	

	#with open("lexicon.txt", "w") as f:
	#	f.write(new_lex)
