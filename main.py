#! /usr/bin/env python

import csv
import re
import sys

def read_file(infile, outfile):
    text = infile.read()

    converter = Converter(output=outfile)
    for line in text.split('\n'):
        converter.convert(line)

class Converter(object):
    def __init__(self, output, error=None):
        if not error:
            error = sys.stderr

        self.output = output
        self.error = error

    def convert(self, line):
        if not line.strip():
            return False

        # Line includes kanji, kana, and reading
        kanji_pattern = r'(.*)\s*\xe3\x80\x90(.*)\xe3\x80\x91\s*(.*)'
        kanji_regex = re.compile(kanji_pattern, re.U)

        # line includes only kana and reading
        kana_pattern = r'^(.*)\t+(.*)$'
        kana_regex = re.compile(kana_pattern, re.U)

        try:
            match = kanji_regex.match(line)

            # Try to match kanji line
            if match:
                groups = match.groups()

                kanji = groups[0].strip()
                kana = groups[1].strip()
                reading = groups[2].strip()

                front = kanji
                back = '{0}<br>{1}'.format(kana, reading)

                self.output.writerow([front, back])

                #print('kanji: ' + line)

                return True

            # Try to match kana only line
            match = kana_regex.match(line)
            if match:
                groups = match.groups()

                kana = groups[0].strip()
                reading = groups[1].strip()

                #print('kana: ' + line)

                self.output.writerow([kana, reading])
                return True

            return False

        except AttributeError as e:
            self.error.write('Error: {0}\n'.format(line))

if __name__ == '__main__':
    args = sys.argv 

    if len(args) != 3:
        print('Usage main.py input')
        sys.exit(1)

    inpath = args[1]
    outpath = args[2]

    infile = open(inpath, 'r')
    outfile = csv.writer(open(outpath, 'w'))
    read_file(infile, outfile)
    
