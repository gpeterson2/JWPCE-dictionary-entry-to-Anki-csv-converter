#! /usr/bin/env python

''' Converts a file of JWPCE dictionary defenitions to an Anki CSV.

    *Note* The file must start in utf-8 format, not the default JWPCE format.
    At some point this may change, but for the moment I don't want to deal
    with the various file encodings.
'''

import csv
import re
import sys

class ConvertError(Exception):
    ''' Error when line can't be converted '''
    pass

def read_file(inpath):
    ''' Given a filepath converts the lines in the file. 

        Will return a list of the conversions.

        :param inpath: The path to a file to open.
        :returns: A list of converted lines.
    '''

    contents = []
    with open(inpath, 'r') as infile:
        for line in infile.readlines():
            if not line.strip():
                continue

            converted = None
            try:
                converted = convert(line)
            except ConvertError:
                pass

            if converted:
                contents.append(converted)

    return contents

def write_file(outpath, contents):
    ''' Writes converted lines to a csv. '''

    f = open(outpath, 'w')
    writer = csv.writer(f)

    for front, back in contents:
        writer.writerow([front, back])

    f.close()

def convert(line):
    ''' Parses a JWPCE line into a front, and back flashcard format.

        Capable of being imported into Anki.

        There are two types dictionary lines:
        1. kanji [kana] defenition
        2. kana defenition

        This will determine which is it is and in case one return:
        front: kanji, back: kana newline defenitions

        in the case of a kana line it will return:
        front: kana, back: defenitions    

        Will throw a ConvertError if the line doesn't match.

        :param line: A JWPCE dictionary line.
    '''

    front = ''
    back = ''

    # Line includes kanji, kana, and reading
    kanji_pattern = r'(.*)\s*\xe3\x80\x90(.*)\xe3\x80\x91\s*(.*)'
    kanji_regex = re.compile(kanji_pattern, re.U)

    # line includes only kana and reading
    kana_pattern = r'^(.*)\t+(.*)$'
    kana_regex = re.compile(kana_pattern, re.U)

    match = kanji_regex.match(line)

    # TODO - the return from the kanji section smells bad. There should be a
    # way to determine which line matches perform the logic, and have only
    # a single return.
    # Ideally there could be one regex to match both.

    # Try to match kanji line
    if match:
        groups = match.groups()

        kanji = groups[0].strip()
        kana = groups[1].strip()
        reading = groups[2].strip()

        front = kanji
        back = '{0}<br>{1}'.format(kana, reading)

        return (front, back)

    # Try to match kana only line
    match = kana_regex.match(line)
    if match:
        groups = match.groups()

        kana = groups[0].strip()
        reading = groups[1].strip()

        return (kana, reading)

    raise ConvertError('Line not matched')

if __name__ == '__main__':
    args = sys.argv 

    if len(args) != 3:
        print('Usage main.py input')
        sys.exit(1)

    inpath = args[1]
    outpath = args[2]

    contents = read_file(inpath)
    write_file(outpath, contents) 

