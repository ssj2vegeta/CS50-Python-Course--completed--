from tabulate import tabulate

import sys
import csv
masterlist = []
if len(sys.argv) == 1:
    raise Exception("invalid")
if len(sys.argv) == 2:
    if ".csv" not in sys.argv[1]:
        raise Exception("invalid")
    else:
        try:
            with open(sys.argv[1], "r") as file:
                reader = csv.reader(file)
                for i in reader:
                    masterlist.append(i)
        except FileNotFoundError:
           raise Exception("invalid")
        finally:
            print(tabulate(masterlist[1:], headers = masterlist[0], tablefmt="grid"))
if len(sys.argv) > 2:
    raise Exception("invalid")