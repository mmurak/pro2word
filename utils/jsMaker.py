import re
import sys

#vset = r'[ɑæʌɔaʊəɚɪɛɝeɨioʊuʉ]'
cset = r'[^btʃdðɾl̩m̩n̩fɡhʒklmnŋɾ̃pʔɹsθvwʍjz]'

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print('Usage:  input dict filename', file=sys.stderr)
        sys.exit(1)
    internalDict = {}
    with open(args[1], 'r') as f:
        for line in f:
            line = line.rstrip()
            sep = line.find('[')       # this is the separator
            entry = line[0:sep-1]
            entry = re.sub(r'\([0-9]\)', '', entry)     # I don't need any (n) notes.
            entry = re.sub(r'^"', '\\"', entry)
            pron = line[sep:]   # 2 is the length of the separator
#            pron = pron.replace('ɚ', 'əɹ')          # SPECIAL TREATMENT for rhotacized vowel
#            pron = pron.replace('ɝ', 'ɜɹ')          # SPECIAL TREATMENT for rhotacized vowel
            pron = re.sub(r'[\[\]]', '', pron)
##            pron = pron.replace('\u0300', '')       # remove grave accent
##            pron = pron.replace('\u0301', '')       # remove acute accent
#            conly = re.sub(cset, '', pron)      # remove all vowels
#            internalDict.setdefault(conly, '')
#            internalDict[re.sub(cset, '', pron)] += entry + '>'  #  '>' = separator symbol
            internalDict.setdefault(pron, '')
            internalDict[pron] += entry + '>'  #  '>' = separator symbol
    print('const iDict = {')
    for i in internalDict:
        entryList = internalDict[i][:-1]
        entrySet = set()
        for es in entryList.split('>'):
            entrySet.add(f'"{es}"')
        print('"' + i + '": [' + ','.join(entrySet) + '],')
    print('};')

