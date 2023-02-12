import pytest
from jar import Jar

def test_construct():
    jar = Jar()
    print(jar.capacity)

def test_str():
    jar = Jar(5)
    jar.jarsize = 5
    assert str(jar) == "🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.jarsize == 5
    with pytest.raises(ValueError):
        jar.deposit(13)


def test_withdraw():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(2)
    assert jar.jarsize == 9
    with pytest.raises(ValueError):
        jar.withdraw(111)




