import pytest
from code_challenges.sorting.insertion.insertion_sort import insertion_sort

def test_average_case():
    avg_list = [8,4,23,42,16,15]
    actual = insertion_sort(avg_list)
    expected = [4,8,15,16,23,42]
    assert actual == expected


def test_empty_list():
    empty_list = []
    actual = insertion_sort(empty_list)
    expected = []
    assert actual == expected


def test_one_element_list():
    one_item = [5]
    actual = insertion_sort(one_item)
    expected = [5]
    assert actual == expected


def test_reverse_sorted():
    rev_list = [20,18,12,8,5,-2]
    actual = insertion_sort(rev_list)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_few_uniques():
    samesies_list = [5,12,7,5,5,7]
    actual = insertion_sort(samesies_list)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_nearly_sorted():
    samesies_list = [2,3,5,7,13,11]
    actual = insertion_sort(samesies_list)
    expected = [2,3,5,7,11,13]
    assert actual == expected
