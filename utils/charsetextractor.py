import re
import sys

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print('Usage:  input-dictionary-filename', file=sys.stderr)
        sys.exit(1)
    internalDict = set()
    with open(args[1], 'r') as f:
        for line in f:
            line = line.rstrip()
            m = re.findall(r'\[(.+?)\]', line)
            nline = m[0]
            nline = nline.replace('\u0300', '')
            nline = nline.replace('\u0301', '')
            for ch in nline:
                if ch == 'N':
                    print(line, file=sys.stderr)
                internalDict.add(ch)
    print(''.join(internalDict))

#  pktmvrwθfʃʒdzŋsjðlnɡbh
#  əʌiɔouʊɚɪɛɑæae