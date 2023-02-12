import um
import pytest

def test_word():
    assert um.count("lum") == 0
    assert um.count("um, um") == 2

def test_space():
    assert um.count("um,um") == 2

def test_caseinsesitivity():
    assert um.count("Um,um") == 2