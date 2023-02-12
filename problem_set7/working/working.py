import re
import sys
def main():
    print(convert(input("Hours: ")))
def convert(s):
    hlist = []
    minlist = []
    masterstring = ""
    match = re.search("^([0-9]|1[0-2]):?([0-5][0-9])? (?:AM|PM) to ([0-9]|1[0-2]):?([0-6][0-9])? (?:AM|PM)$", s)
    if match:
        slist = s.split(" to ")
        for i in slist:
            count = 0
            for j in i:
                if j == " " or j == ":":
                    if j == ":":
                        minlist.append((i[count+1:count+3]))
                    else:
                        minlist.append("00")
                    if "PM" in i:
                        hlist.append(str(int(i[0:count]) + 12))
                        break
                    elif "AM" in i:
                        hlist.append(str(int(i[0:count])))
                        break
                else:
                    count += 1
                    continue
        for i in range(2):
            if int(hlist[i]) < 10:
                hlist[i] = "0" + hlist[i]
            masterstring = masterstring + hlist[i] + ":" + minlist[i]
            if i < 1:
                masterstring = masterstring + " to "

        return masterstring
    else:
        raise ValueError

if __name__ == "__main__":
    main()