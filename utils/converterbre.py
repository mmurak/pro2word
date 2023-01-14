import re
import sys


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print('Usage:  input-dictionary-filename', file=sys.stderr)
        sys.exit(1)
    vowels = 'ɛɒɪɐəæɜeauɔɑiʊ'
    prim = re.compile('ˈ(.)')
    second = re.compile('ˌ(.)')
    patV =  re.compile(f'^[{vowels}]+$')
    patCV =  re.compile(f'^[^{vowels}]+[{vowels}]+$')
    patVC =  re.compile(f'^[{vowels}]+[^{vowels}]+$')
    patCVC =  re.compile(f'^[^{vowels}]+[{vowels}]+[^{vowels}]+$')
    with open(args[1], 'r', encoding='utf-8') as f:
        of = open(args[1]+'.out.txt', 'w', encoding='utf-8')
        for line in f:
            line = line.strip()
            sep = line.find(',')       # first space is the separator
            entry = line[0:sep]
            entry = entry.replace('_', ' ').lower()
            pron = line[sep + 1:]   # 1 is the length of the separator
            pron = pron.strip()
            pron = pron.replace('g', 'ɡ')
            pron = pron.replace(' ', '')
            pron = re.sub(prim, r'\1U0301', pron)
            pron = pron.replace('U0301', '\u0301')
            pron = re.sub(second, r'\1U0300', pron)
            pron = pron.replace('U0300', '\u0300')
            if re.match(patV, pron) or re.match(patCV, pron) or re.match(patVC, pron) or re.match(patCVC, pron):
                pron = pron.replace('\u0301', '')
            of.writelines(entry + ',[' + pron + ']\n')
        of.close()
