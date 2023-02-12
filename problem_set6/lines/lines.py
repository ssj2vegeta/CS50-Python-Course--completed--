import sys

if len(sys.argv) == 1:
    raise Exception("invalid")
    sys.exit()
if len(sys.argv) == 2:
    if ".py" not in sys.argv[1]:
        raise Exception("invalid")
        sys.exit()
    else:
        count = 0
        try:
            with open(sys.argv[1], "r") as file:
                for i in file:
                    i = i.strip()
                    if len(i) == 0:
                        continue
                    elif i[0] == "#":
                        continue
                    else:
                        count += 1
        except FileNotFoundError:
            print("File deos not exist")
            sys.exit()
        print(count)
        sys.exit()




if len(sys.argv) > 2:
    raise Exception("invalid")
    sys.exit()