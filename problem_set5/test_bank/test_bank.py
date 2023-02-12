from bank import value

def main():
    test_greeting1()


def test_greeting1():
    assert value("hello") == 0
    assert value("hdeeznuts") == 20
    assert value("no") == 100
    assert value("HELLO") == 0
    assert value("HEY") == 20


if __name__ == "__main__":
    main()