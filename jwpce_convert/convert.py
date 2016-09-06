#! /usr/bin/env python

import csv
import re

__all__ = ['convert', 'read_file', 'write_file']


class ConvertError(Exception):
    ''' Error when line can't be converted '''
    pass


def read_file(inpath):
    ''' Given a filepath converts the lines in the file.

        Will return a list of the conversions.

        :param inpath: The path to a file to open.
        :returns: A list of converted lines.
    '''

    with open(inpath, 'r') as infile:
        for line in infile.readlines():
            # ignore empty lines
            if not line.strip():
                continue

            line = line.decode('utf-8')

            try:
                converted = convert(line)
                # Returns front/back and back/front
                for item in converted:
                    yield item
            except ConvertError:
                pass


def write_file(outpath, contents):
    ''' Writes converted lines to a csv. '''

    with open(outpath, 'w') as f:
        writer = csv.writer(f)

        for front, back in contents:
            writer.writerow([front.encode('utf-8'), back.encode('utf-8')])


# TODO - this should probably work on a list rather than/including a line
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

    # Line includes kanji, kana, and reading
    kanji_pattern = r'(.*)\s*\xe3\x80\x90(.*)\xe3\x80\x91\s*(.*)'
    kanji_regex = re.compile(kanji_pattern, re.U)

    # line includes only kana and reading
    kana_pattern = r'^(.*)\t+(.*)$'
    kana_regex = re.compile(kana_pattern, re.U)

    # TODO - the return from the kanji section smells bad. There should be a
    # way to determine which line matches perform the logic, and have only
    # a single return.
    # Ideally there could be one regex to match both.

    # Try to match kanji line
    match = kanji_regex.match(line)
    if match:
        groups = match.groups()

        kanji = groups[0].strip()
        kana = groups[1].strip()
        # Wasn't removing characters correctly.
        # TODO - decode/encode when reading/writing.
        reading = groups[2].strip()

        kanji_front = kanji
        kanji_back = '{}<br>{}'.format(kana, reading)

        # TODO - might have issues with readings that are the same.
        english_front = reading
        english_back = '{}<br>{}'.format(kanji, kana)

        return [(kanji_front, kanji_back), (english_front, english_back)]

    # Try to match kana only line
    match = kana_regex.match(line)
    if match:
        groups = match.groups()

        kana = groups[0].strip()
        reading = groups[1].strip()

        return [(kana, reading), (reading, kana)]

    raise ConvertError('Line not matched')
