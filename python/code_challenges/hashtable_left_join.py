from data_structures.hashtable import Hashtable


def left_join(hash_a, hash_b):
    thesaurus = Hashtable()
    for key in hash_a.keys():
        a_value = hash_a.get(key)
        b_value = None
        if hash_b.contains(key):
            b_value = hash_b.get(key)
        thesaurus.set(key, (a_value, b_value))
    return thesaurus


