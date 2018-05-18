

if __name__ == "__main__":
	with open("utt2spk", "w") as f:
		for i in range(1,87):
			if i < 10:
				f.write("allende0" + str(i) + "-allende allende")
			else:
				f.write("allende" + str(i) + "-allende allende")
			f.write("\n")
