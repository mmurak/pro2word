import re
dict = {}
with open('Gutenberg.txt') as f:
	for sline in f:
		if re.match(r'^#', sline):
			continue
		word = sline.split("\t")
		if (len(word) != 3):
			exit()
		if re.match(r'[^a-z]', word[1]):
#			print(word[1])
			continue
#		print(word[1])
		dict[word[1]] = 1
print("// Most common English words in Project Gutenberg (2006, 2005) -- (https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/English )")
print("const WordList = [")
for k in dict.keys():
	print(f'\t"{k}",')
print("];")

