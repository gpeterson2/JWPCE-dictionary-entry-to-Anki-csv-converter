#! /usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import re

__all__ = ['convert', 'read_file', 'write_file']


class ConvertError(Exception):
    ''' Error when line can't be converted. '''

    pass


def read_file(inpath):
    ''' Given a filepath converts the lines in the file.

        This will return a generator of converted values.

        :param str inpath: The path to a file to open.
        :returns: A generator of converted lines.
    '''

    with open(inpath, 'r', encoding='utf-8') as infile:
        for line in infile.readlines():
            # ignore empty lines
            if not line.strip():
                continue

            try:
                converted = convert(line)
                # Returns front/back and back/front
                for item in converted:
                    yield item
            except ConvertError:
                pass


def write_file(outpath, contents):
    ''' Writes converted lines to a csv.

        :param str outpath: The filepath to write to.
        :param contents: An iterable to write.
    '''

    with open(outpath, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)

        for front, back in contents:
            writer.writerow([front, back])


def convert(line):
    ''' Parses a JWPCE line into a front, and back flashcard format.

        Capable of being imported into Anki.

        There are two types dictionary lines:
        1. kanji [kana] definition
        2. kana definition

        This will determine which is it is and return appropriate front and
        back values as well as the invertend values to esure that both
        Japanaese to English as well as English to Japanese knowledge is
        tested.

        For example it will return a kana front and English back as well as an
        English front and kana back.

        In the case of a kanji line it will return return::

            [
                (kanji, kana newline definitions),
                (definitions, kanji newline kana),
            ]

        in the case of a kana line it will return::

            [
                (kana, definitions),
                (definition, kana),
            ]

        This sill throw a ConvertError if the line doesn't match.

        :param line: A JWPCE dictionary line.
        :returns: List of matched tuples
        :rtype: list
        :raises: ConvertError
    '''

    regular = None
    inverted = None

    # Line includes kanji, kana, and reading
    # line includes only kana and reading
    # (?: means ignore that as a match.
    pattern = r'^(\w*)\s*(?:【(\w*)】)?\s*(.*)$'

    # TODO - The re.U option may not be required in which case the pattern
    # could be tested directly, otherwise the compile should happen outside
    # this function so that is only done once.
    kanji_regex = re.compile(pattern, re.U)

    match = kanji_regex.match(line)
    if not match:
        raise ConvertError('Line not matched')

    groups = match.groups()

    # Either won't return groups or will match nothing as: '', None, ''
    if len(groups) != 3 or groups[0] == '':
        raise ConvertError('Line not matched')

    # If this exists it means the part in 【】 matched
    if groups[1] is not None:

        kanji = groups[0].strip()
        kana = groups[1].strip()
        reading = groups[2].strip()

        kanji_front = kanji
        kanji_back = '{0}<br>{1}'.format(kana, reading)

        # TODO - might have issues with readings that are the same.
        english_front = reading
        english_back = '{0}<br>{1}'.format(kanji, kana)

        regular = (kanji_front, kanji_back)
        inverted = (english_front, english_back)

    # Otherwise assume it was a kana match
    else:
        kana = groups[0].strip()
        reading = groups[2].strip()

        regular = (kana, reading)
        inverted = (reading, kana)

    return [regular, inverted]
