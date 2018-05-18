
## change lexicon from having a * to an entry for each spanish vowel
## instead of the *

if __name__ == "__main__":
	spanish_vowels = ["a", "e", "i", "o", "u", "aw", "ay", "ey", "oy"]

	english_pronounce = open("english_pronounce.txt", "r")
	english_words = open("/projects/speech/sys/kaldi/egs/word/allende/data/train-allende/words", "r")
	
	pronounce = english_pronounce.read()
	english_pronounce.close()
	words = english_words.read()
	english_words.close()

	pronounce = pronounce.split("\n")
	words = words.split("\n")
	
	out = ""

	for i in range(len(words)):
		out = out + words[i] + "\t" + pronounce[i] + "\n"


	out_lines = out.split("\n")
	
	out2 = ""
	for line in out_lines:
		if line == "":
			continue
		cur_word = line.split("\t")[0]
		cur_pronounce = line.split("\t")[1]
		if "*" in cur_pronounce:
			for vowel in spanish_vowels:
				out2 = out2 + cur_word + "\t" + cur_pronounce.replace("*", vowel) + "\n" 
		else:
			out2 = out2 + cur_word + "\t" + cur_pronounce + "\n"
			
			
	with open("english_lexicon.txt", "w") as f:
		f.write(out2)
		

	
