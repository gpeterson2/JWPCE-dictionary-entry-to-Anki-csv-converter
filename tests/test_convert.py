# -*- coding: utf-8 -*-

from jwpce_convert.convert import convert, ConvertError


class TestConvert:

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
        line = 'ずっと	(adv) (1) direct, straight, (2) all along, the whole time, all the way, (3) for a long time, throughout, (4) by far, far and away, (P)'

        kana = 'ずっと'
        reading = '(adv) (1) direct, straight, (2) all along, the whole time, all the way, (3) for a long time, throughout, (4) by far, far and away, (P)'

        result = convert(line)

        expected = [
            (kana, reading),
            (reading, kana),
        ]

        assert result == expected

    def test_covert_failure(self):
        passed = False
        line = ''

        try:
            result = convert(line)
        except ConvertError:
            passed = True

        assert passed is True
