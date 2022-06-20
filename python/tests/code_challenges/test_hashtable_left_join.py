import pytest
from code_challenges.hashtable_left_join import left_join
from data_structures.hashtable import Hashtable


def test_exists():
    assert left_join


# @pytest.mark.skip("TODO")
def test_example():
    synonyms = Hashtable()
    synonyms.set("fond", "enamored")
    synonyms.set("wrath", "anger")
    synonyms.set("diligent", "employed")
    synonyms.set("outfit", "garb")
    synonyms.set("guide", "usher")

    antonyms = Hashtable()
    antonyms.set("fond", "averse")
    antonyms.set("diligent", "idle")
    antonyms.set("guide", "follow")
    antonyms.set("flow", "jam")
    antonyms.set("wrath", "delight")

    expected = Hashtable()
    expected.set("fond", ("enamored", "averse"))
    expected.set("wrath", ("anger", "delight"))
    expected.set("diligent", ("employed", "idle"))
    expected.set("outfit", ("garb", None))
    expected.set("guide", ("usher", "follow"))

    actual = left_join(synonyms, antonyms)

    assert actual == expected
