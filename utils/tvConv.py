import re
with open('tv.txt') as f:
	for sline in f:
		if re.match(r'^#', sline):
			continue
		word = sline.split("\t")
		w = word[1].split(" ")
		if re.match(r'^[a-z]+$', w[0]):
			print(w[0])