from twttr import shorten
def main():
    test_shorten1()
    test_shorten2()
    test_shorten3()
def test_shorten1():
    assert shorten("ding") == "dng"

def test_shorten2():
    assert shorten("DEEZ") == "DZ"

def test_shorten3():
    assert shorten("#28839829,AEIOU") == "#28839829,"



if __name__ == "__main__":
    main()

