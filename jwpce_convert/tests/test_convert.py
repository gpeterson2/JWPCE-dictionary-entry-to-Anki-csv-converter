# -*- coding: utf-8 -*-

import unittest

from jwpce_convert.convert import convert, ConvertError


class TestConvert(unittest.TestCase):

    def test_convert_kanji(self):
        line = '種類	【しゅるい】	(n) variety, kind, type, category, counter for different sorts of things, (P)'

        kanji = '種類'
        kana = 'しゅるい'
        reading = '(n) variety, kind, type, category, counter for different sorts of things, (P)'

        result = convert(line)

        expected = [
            (kanji, '{}<br>{}'.format(kana, reading)),
            (reading, '{}<br>{}'.format(kanji, kana)),
        ]

        assert result == expected

    def test_covert_kana(self):
        # E501 These are long lines, but I don't want to alter the line becasue
        # that is what would be found in the file itself.
        line = 'ずっと	(adv) (1) direct, straight, (2) all along, the whole time, all the way, (3) for a long time, throughout, (4) by far, far and away, (P)'  # noqa: E501

        kana = 'ずっと'
        reading = '(adv) (1) direct, straight, (2) all along, the whole time, all the way, (3) for a long time, throughout, (4) by far, far and away, (P)'  # noqa: E501

        result = convert(line)

        expected = [
            (kana, reading),
            (reading, kana),
        ]

        assert result == expected

    def test_covert_failure(self):
        with self.assertRaises(ConvertError):
            convert('')
