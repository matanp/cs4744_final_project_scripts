import re
import string
import sys
import json


if __name__ == "__main__":
	transcript = open('../text', 'r')
	
	text = transcript.read()

	word_count = {}

	for line in text.split("\n"):
		words = line.split(" ")
		for i in range(len(words)):
			if i < 1:
				continue
			else:
				word = words[i]
				word = word.translate(None, string.punctuation)
				if word in word_count:
					word_count[word] += 1
				else:
					word_count[word] = 1 

	#print(json.dumps(word_count, indent=2))
	
	with open('words', 'w') as f:		
		for word, count in sorted(word_count.items()):
			f.write(word + "\n")	
		
	transcript.close()
