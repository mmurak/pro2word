import re
import sys

class ARPABETconverter:
    # https://en.wikipedia.org/wiki/CMU_Pronouncing_Dictionary
    specialTreatment = [
        ['AH0', 'ə'], 
    ]
    vset = [
        ['AA', 'ɑ'], ['AE', 'æ'], ['AH', 'ʌ'], ['AO', 'ɔ'], ['AW', 'aʊ'], ['AY', 'aɪ'], ['EH', 'ɛ'],
        ['ER', 'ɚ'], ['EY', 'eɪ'], ['IH', 'ɪ'], ['IY', 'i'], ['OW', 'oʊ'], ['OY', 'ɔɪ'], ['UH', 'ʊ'], ['UW', 'u'],
        # primary \u0301
        ['AA1', 'ɑ\u0301'], ['AE1', 'æ\u0301'], ['AH1', 'ʌ\u0301'], ['AO1', 'ɔ\u0301'], 
        ['AW1', 'a\u0301ʊ'], ['AY1', 'a\u0301ɪ'], ['EH1', 'ɛ\u0301'],
        ['ER1', 'ɚ\u0301'], ['EY1', 'e\u0301ɪ'], ['IH1', 'ɪ\u0301'], ['IY1', 'i\u0301'], ['OW1', 'o\u0301ʊ'],
        ['OY1', 'ɔ\u0301ɪ'], ['UH1', 'ʊ\u0301'], ['UW1', 'u\u0301'],
        # secondary \u0300
        ['AA2', 'ɑ\u0300'], ['AE2', 'æ\u0300'], ['AH2', 'ʌ\u0300'], ['AO2', 'ɔ\u0300'],
        ['AW2', 'a\u0300ʊ'], ['AY2', 'a\u0300ɪ'], ['EH2', 'ɛ\u0300'],
        ['ER2', 'ɚ\u0300'], ['EY2', 'e\u0300ɪ'], ['IH2', 'ɪ\u0300'], ['IY2', 'i\u0300'], ['OW2', 'o\u0300ʊ'],
        ['OY2', 'ɔ\u0300ɪ'], ['UH2', 'ʊ\u0300'], ['UW2', 'u\u0300'],
    ]
    cset = [
        ['B', 'b'], ['CH', 'tʃ'], ['D', 'd'], ['DH', 'ð'],
        ['F', 'f'], ['G', 'ɡ'],
        ['HH', 'h'], ['JH', 'dʒ'], ['K', 'k'], ['L', 'l'],
        ['M', 'm'], ['N', 'n'], ['NG', 'ŋ'], ['P', 'p'],
        ['R', 'r'], ['S', 's'], ['SH', 'ʃ'], ['T', 't'],
        ['TH', 'θ'], ['V', 'v'], ['W', 'w'], ['Y', 'j'],
        ['Z', 'z'], ['ZH', 'ʒ'],
    ]
    vowels = 'iueəʌɔaɪʊɛɚɑoæ\u0301'

# constructor
    def __init__(self):
        self.specialData = []
        for entry in ARPABETconverter.specialTreatment:
            self.specialData.append([' '+entry[0]+' ', ' '+entry[1]+' '])
        self.data = []
        for entry in ARPABETconverter.vset:
            self.data.append([' '+entry[0]+' ', ' '+entry[1]+' '])
        for entry in ARPABETconverter.cset:
            self.data.append([' '+entry[0]+' ', ' '+entry[1]+' '])
        self.patternV = re.compile(f'^[{ARPABETconverter.vowels}]+$')
        self.patternCV = re.compile(f'^[^{ARPABETconverter.vowels}]+[{ARPABETconverter.vowels}]+$')
        self.patternVC = re.compile(f'^[{ARPABETconverter.vowels}]+[^{ARPABETconverter.vowels}]+$')
        self.patternCVC = re.compile(f'^[^{ARPABETconverter.vowels}]+[{ARPABETconverter.vowels}]+[^{ARPABETconverter.vowels}]+$')
# conversion function
    def convert(self, code):
        codeWsentinel = ' ' + code + ' '
        for entryPair in self.specialData:
            codeWsentinel = codeWsentinel.replace(entryPair[0], entryPair[1])
        codeWsentinel = codeWsentinel.replace('0', '')
        for entryPair in self.data:
            codeWsentinel = codeWsentinel.replace(entryPair[0], entryPair[1])
        for entryPair in self.data:     # need to do this again for [nN] boundary problem.
            codeWsentinel = codeWsentinel.replace(entryPair[0], entryPair[1])
        finalOut = codeWsentinel.replace(' ', '')
        if re.match(self.patternV, finalOut) or re.match(self.patternCV, finalOut) or re.match(self.patternVC, finalOut) or re.match(self.patternCVC, finalOut):
            finalOut = finalOut.replace('\u0301', '')
        return finalOut

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print('Usage:  input-dictionary-filename', file=sys.stderr)
        sys.exit(1)
    converter = ARPABETconverter()
    with open(args[1], 'r') as f:
        of = open(args[1]+'.out.txt', 'w')
        for line in f:
            line = line.rstrip()
            sep = line.find(' ')       # first space is the separator
            entry = line[0:sep]
            pron = line[sep + 1:]   # 1 is the length of the separator
            pron = re.sub(r'#.*$', '', pron)
            of.writelines(entry + ',[' + converter.convert(pron) + ']\n')
        of.close()
