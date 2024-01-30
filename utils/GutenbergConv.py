import re
with open('Gutenberg.txt') as f:
	for sline in f:
		if re.match(r'^#', sline):
			continue
		word = sline.split("\t")
		if (len(word) != 3):
			exit()
		print(word[1])