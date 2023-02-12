import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    findall = re.findall(r"\b(u|U)m\b", s)
    return len(findall)


...


if __name__ == "__main__":
    main()