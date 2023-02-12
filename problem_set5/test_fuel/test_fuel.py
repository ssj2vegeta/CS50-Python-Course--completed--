import pytest
from fuel import convert, gauge
def main():
    test()
def test():
    assert convert('1/4') == 25 and gauge(25) == "25%"
    assert convert('1/100') == 1 and gauge(1) == "E"
    assert convert('99/100') == 99 and gauge(99) == "F"
def test2():
    with pytest.raises(ZeroDivisionError):
         convert('1/0')
    with pytest.raises(ValueError):
         convert('two/four')
def test3():
    with pytest.raises(ValueError):
         convert('cat/dog')

if __name__ == "__main__":
    main()