
###look at an alignment file and turn all the numbers into phones based
## on phones.txt

if __name__ == "__main__":
	with open("phones.txt", "r") as f:
		phones = f.read()

	phones = phones.split("\n")

	#set up phones array so phones[i] contains the phone corresponding
	#to number i+1 in the alignment files
	for i in range(len(phones)):
		phones[i] = phones[i].split(" ")[0]

	with open("show_ali_1.txt", "r") as f:
		ali_1 = f.read()

	ali_1 = ali_1.split("\n")
	final_phones = ""
	last_id = ""
	for i in range(len(ali_1)):
		cur_id = ali_1[i].split(" ")[0]
		if cur_id == last_id or cur_id.strip() == "":
			continue
		last_id = cur_id
		cur_ali = ali_1[i].split(" ")[2:]	
		cur_phones = ""

		for j in range(len(cur_ali)):
			try:
				phone_index = int(cur_ali[j])
				if phone_index > len(phones):
					cur_phones = cur_phones + " ?"
				else:
					cur_phones = cur_phones + " " + phones[phone_index - 1]
			except ValueError:
				cur_phones = cur_phones + " " + cur_ali[j]

		final_phones = final_phones + cur_id + "  " + cur_phones + "\n"	

	with open("phones_out.txt", "w") as f:
		f.write(final_phones)

		
