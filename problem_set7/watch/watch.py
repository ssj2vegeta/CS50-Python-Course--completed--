import re
import sys
# src="(https?://(www)?.youtube.com/)embed/(xvFZjo5PgG0)".+></iframe$

def main():
    print(parse(input("HTML: ")))


def parse(s):
    m = re.search('.+src="https?://(?:www.)?youtube.com/embed/(.+?)"', s)
    if m:
        masterstring = "https://youtu.be/" + m.group(1)
        return masterstring
    else:
        return None
...


if __name__ == "__main__":
    main()