from working import convert
import pytest

def testrange():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_wrong_format():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")
def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("13 PM to 17 PM")
def wrong_minute():
    with pytest.raises(ValueError):
        convert("11:60 PM to 17:70 PM")
