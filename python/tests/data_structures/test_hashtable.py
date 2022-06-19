import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable

def test_create():
    hashtable = Hashtable()
    actual = hashtable.size
    expected = 1024
    assert actual == expected

def test_valid():
    hashtable = Hashtable()
    index = hashtable.hash('spanikopita')
    assert 0 <= index < hashtable.size

def test_set_spanikopita():
    hashtable = Hashtable()
    hashtable.set('greek dish', 'spanikopita')
    greek_index = hashtable.hash('greek dish')
    actual = hashtable._buckets[greek_index]
    expected = ('greek dish', 'spanikopita')
    assert actual.head.value == expected


def test_get_spanikopita():
    hashtable = Hashtable()
    hashtable.set("spanikopita", "Flaky spinach and feta dish")
    actual = hashtable.get("spanikopita")
    expected = "Flaky spinach and feta dish"
    assert actual == expected

def test_handle_collisions():
    ht = Hashtable()
    ht.set('rat','a snitch')
    ht.set('tar','and feather')
    ht.set('tra','la la la la')
    assert ht.get('rat') == ('a snitch')
    assert ht.get('tar') == ('and feather')
    assert ht.get('tra') == ('la la la la')

def test_contains():
    hashtable = Hashtable()
    hashtable.set('greek dish', 'spanikopita')
    expected = True
    actual = hashtable.contains('greek dish')
    assert actual == expected

def test_does_not_contain():
    hashtable = Hashtable()
    hashtable.set('act', 'or do not, that is the question')
    expected = False
    actual = hashtable.contains('tac')
    assert actual == expected

def test_keys():
    hashtable = Hashtable()
    hashtable.set('rat','a snitch')
    hashtable.set('tar','and feather')
    hashtable.set('tra','la la la la')
    actual = hashtable.keys()
    expected = {'rat','tar','tra'}
    assert actual == expected
