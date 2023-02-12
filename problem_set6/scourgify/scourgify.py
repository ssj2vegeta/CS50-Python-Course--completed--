import sys
import csv
masterlist = []
if len(sys.argv) < 3:
    raise Exception("invalid")
if len(sys.argv) == 3:
    if ".csv" not in sys.argv[1]:
        raise Exception("invalid")
    else:
        try:
            with open(sys.argv[1], "r") as file:
                reader = csv.DictReader(file)
                for i in reader:
                   split_name = i["name"].split(",")
                   masterlist.append({"first": split_name[1].strip(), "last":split_name[0], "house": i["house"]})
            f = open(sys.argv[2], "x")
            with open(sys.argv[2], "w") as file:
                writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
                writer.writerow({"first": "first", "last": "last", "house": "house"})
                for row in masterlist:
                    writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})
        except FileNotFoundError:
           raise Exception("invalid")
if len(sys.argv) > 3:
    raise Exception("invalid")