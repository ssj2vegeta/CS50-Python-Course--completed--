from seasons import validator
import pytest

def test():
    assert validator("1999-12-12") == "Twelve million, one hundred seventy-six thousand, six hundred forty minutes"