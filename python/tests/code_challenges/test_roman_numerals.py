import pytest
from code_challenges.roman_numerals import roman_numerals

def test_empty_string():
    romans = ""
    actual = roman_numerals(romans)
    expected = 0
    assert actual == expected


def test_single_character():
    romans = "V"
    actual = roman_numerals(romans)
    expected = 5
    assert actual == expected


def test_invalid_numerals():
    romans = "NOPE"
    with pytest.raises(Exception):
        roman_numerals(romans)


def test_lower_case():
    romans = "vLmM"
    actual = roman_numerals(romans)
    expected = 1945
    assert actual == expected


def test_normal_roman_numeral():
    romans = "MMXXII"
    actual = roman_numerals(romans)
    expected = 2022
    assert actual == expected
