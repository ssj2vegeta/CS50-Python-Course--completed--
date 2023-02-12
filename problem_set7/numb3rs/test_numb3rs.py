from numb3rs import validate
import pytest


def test_format():
    assert validate(r"25.25.25") == False
    assert validate(r"25.25") == False
    assert validate(r"25.25.25.25") == True
    assert validate(r"25") == False

def test_range():
    assert validate(r"255.255.255.255") == True
    assert validate(r"1000.255.255.255") == False
    assert validate(r"255.1000.255.255") == False
    assert validate(r"255.255.1000.255") == False
    assert validate(r"255.255.255.1000") == False
