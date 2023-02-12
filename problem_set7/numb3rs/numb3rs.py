
import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ipt = re.search("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip)
    if ipt:
        try:
            iplist = ip.split(".")
        except:
            return False
        finally:
            for i in iplist:
                if int(i) < 0 or int(i) > 255:
                    return False
            return True
    else:
        return False



...


if __name__ == "__main__":
    main()