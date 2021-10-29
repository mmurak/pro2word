import re
import sys

class ARPABETconverter:
    vset = [
        ['AA', 'ɑ'], ['AE', 'æ'], ['AH', 'ʌ'], ['AO', 'ɔ'], ['AW', 'aʊ'],
        ['AX', 'ə'], ['AXR', 'ɚ'], ['AY', 'aɪ'], ['EH', 'ɛ'], ['ER', 'ɝ'],
        ['EY', 'eɪ'], ['IH', 'ɪ'], ['IX', 'ɨ'], ['IY', 'i'], ['OW', 'oʊ'],
        ['OY', 'ɔɪ'], ['UH', 'ʊ'], ['UW', 'u'], ['UX', 'ʉ'],
        ['AA1', 'ɑ\u0301'], ['AE1', 'æ\u0301'], ['AH1', 'ʌ\u0301'], ['AO1', 'ɔ\u0301'], ['AW1', 'a\u0301ʊ'],
        ['AX1', 'ə\u0301'], ['AXR1', 'ɚ\u0301'], ['AY1', 'a\u0301ɪ'], ['EH1', 'ɛ\u0301'], ['ER1', 'ɝ\u0301'],
        ['EY1', 'e\u0301ɪ'], ['IH1', 'ɪ\u0301'], ['IX1', 'ɨ\u0301'], ['IY1', 'i\u0301'], ['OW1', 'o\u0301ʊ'],
        ['OY1', 'ɔ\u0301ɪ'], ['UH1', 'ʊ\u0301'], ['UW1', 'u\u0301'], ['UX1', 'ʉ\u0301'],
        ['AA2', 'ɑ\u0300'], ['AE2', 'æ\u0300'], ['AH2', 'ʌ\u0300'], ['AO2', 'ɔ\u0300'], ['AW2', 'a\u0300ʊ'],
        ['AX2', 'ə\u0300'], ['AXR2', 'ɚ\u0300'], ['AY2', 'a\u0300ɪ'], ['EH2', 'ɛ\u0300'], ['ER2', 'ɝ\u0300'],
        ['EY2', 'e\u0300ɪ'], ['IH2', 'ɪ\u0300'], ['IX2', 'ɨ\u0300'], ['IY2', 'i\u0300'], ['OW2', 'o\u0300ʊ'],
        ['OY2', 'ɔ\u0300ɪ'], ['UH2', 'ʊ\u0300'], ['UW2', 'u\u0300'], ['UX2', 'ʉ\u0300'],
    ]
    cset = [
        ['B', 'b'], ['CH', 'tʃ'], ['D', 'd'], ['DH', 'ð'], ['DX', 'ɾ'],
        ['EL', 'l̩'], ['EM', 'm̩'], ['EN', 'n̩'], ['F', 'f'], ['G', 'ɡ'],
        ['HH', 'h'], ['H', 'h'], ['JH', 'dʒ'], ['K', 'k'], ['L', 'l'],
        ['M', 'm'], ['N', 'n'], ['NG', 'ŋ'], ['NX', 'ɾ̃'], ['P', 'p'],
        ['Q', 'ʔ'], ['R', 'ɹ'], ['S', 's'], ['SH', 'ʃ'], ['T', 't'],
        ['TH', 'θ'], ['V', 'v'], ['W', 'w'], ['WH', 'ʍ'], ['Y', 'j'],
        ['Z', 'z'], ['ZH', 'ʒ'],
    ]

# constructor
    def __init__(self):
        self.data = []
        for entry in ARPABETconverter.vset:
            self.data.append([' '+entry[0]+' ', ' '+entry[1]+' '])
        for entry in ARPABETconverter.cset:
            self.data.append([' '+entry[0]+' ', ' '+entry[1]+' '])
# conversion function
    def convert(self, code):
        codeWsentinel = ' ' + code + ' '
        codeWsentinel = codeWsentinel.replace('0', '')
        for entryPair in self.data:
            codeWsentinel = codeWsentinel.replace(entryPair[0], entryPair[1])
        for entryPair in self.data:     # need to do this again for [nN] boundary problem.
            codeWsentinel = codeWsentinel.replace(entryPair[0], entryPair[1])
        return codeWsentinel.replace(' ', '')

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print('Usage:  input dict filename', file=sys.stderr)
        sys.exit(1)
    converter = ARPABETconverter()
    with open(args[1], 'r') as f:
        of = open(args[1]+'.out.txt', 'w')
        for line in f:
            line = line.rstrip()
#1#            if line[0] == ';':          # ; is the comment identifier
#1#                continue
#1#            sep = line.find('  ')       # this 2-space chunk is the separator
            sep = line.find(' ')       # first spece is the separator
            entry = line[0:sep]
#1#            pron = line[sep + 2:]   # 2 is the length of the separator
            pron = line[sep + 1:]   # 1 is the length of the separator
            of.writelines(entry + ',[' + converter.convert(pron) + ']\n')
        of.close()
