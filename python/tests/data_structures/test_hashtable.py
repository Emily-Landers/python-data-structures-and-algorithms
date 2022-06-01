import pytest
from data_structures.hashtable import Hashtable

def test_exists():
    assert Hashtable


def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


def test_set():
    table = Hashtable()
    table.set('cheese', 'blue')

    actual = table.table[470][0]
    expected = ('cheese', 'blue')
    assert actual == expected
    
def test_get():
    table = Hashtable()
    table.set('cheese', 'blue')
    table.set('chese', 'bloo')
    table.set('cheeese', 'bluoe')

    actual = table.get('chese')
    expected = 'bloo'
    assert actual == expected

def test_contains():
    table = Hashtable()
    table.set('cheese', 'blue')

    actual = table.contains('cheese')
    expected = True
    assert actual == expected

def test_hash():
    table = Hashtable()

    actual = table.hash('cheese')
    expected = 28
    assert actual == expected