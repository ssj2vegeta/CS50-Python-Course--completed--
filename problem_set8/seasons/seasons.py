import datetime
import re
import sys
import inflect
p = inflect.engine()
def main():
        result = validator(input("Input the date please: "))
        today = datetime.date.today()
        subtract = today - result
        mins = subtract.days * 24  * 60
        result = p.number_to_words(mins, andword = "") + " minutes"
        print(result.capitalize())
def validator(s):
    dateinput = re.search("^([0-2][0-9][0-9][0-9])-([0-9]?[0-9])-([0-9]?[0-9])$", s)
    if dateinput:
        splitdate = s.split("-")
        try:
            inputdate = datetime.date(int(splitdate[0]), int(splitdate[1]), int(splitdate[2]))
        except:
            sys.exit("Invalid date")
        finally:
            return inputdate
    else:
         sys.exit("Invalid date")


if __name__ == "__main__":
    main()