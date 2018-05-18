
path = "/projects/speech/sys/kaldi/egs/word/allende/data/wav/"

if __name__ == "__main__":
	with open("wav.scp", "w") as f:
		for i in range(1,87):
			if i < 10:
				f.write("allende0" + str(i) + "-allende" + path + "allende0" + str(i) + "-allende.wav")
			else:
				f.write("allende" + str(i) + "-allende" + path + "allende" + str(i) + "-allende.wav")
			f.write("\n")
