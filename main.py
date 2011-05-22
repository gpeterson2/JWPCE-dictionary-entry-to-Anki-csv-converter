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
        if not line:
            return

        pattern = r'(.*)\s*\xe3\x80\x90(.*)\xe3\x80\x91\s*(.*)'
        regex = re.compile(pattern, re.U)

        try:
            match = regex.match(line).groups()

            kanji = match[0].strip()
            kana = match[1].strip()
            reading = match[2].strip()

            front = kanji
            back = '{0}<br>{1}'.format(kana, reading)

            self.output.writerow([front, back])

        except AttributeError as e:
            self.error.write('{0}\n'.format(line))

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
    
