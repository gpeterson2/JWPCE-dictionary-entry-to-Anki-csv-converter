# -*- coding: utf-8 -*-

import pytest

from jwpce_convert.jwpce_convert.convert import convert, ConvertError


class TestConvert:

    def test_jwpce_convert_kanji(self):
        line = '種類	【しゅるい】	(n) variety, kind, type, category, counter for different sorts of things, (P)'

        kanji = '種類'
        kana = 'しゅるい'
        reading = '(n) variety, kind, type, category, counter for different sorts of things, (P)'

        result = convert(line)

        expected = [
            (kanji, f'{kana}<br>{reading}'),
            (reading, f'{kanji}<br>{kana}')
        ]

        assert result == expected

    def test_non_jwpce_convert_kanji(self):
        line = '両親 [りょうしん, ふたおや] (n) parents, both parents'

        kanji = '両親'
        kana = 'りょうしん, ふたおや'
        reading = '(n) parents, both parents'

        result = convert(line)

        expected = [
            (kanji, f'{kana}<br>{reading}'),
            (reading, f'{kanji}<br>{kana}')
        ]

        assert result == expected

    def test_convert_url(self):
        with pytest.raises(ConvertError):
            convert('https://example.com/...')

    def test_convert_failure_empty_line(self):
        with pytest.raises(ConvertError):
            convert('')
