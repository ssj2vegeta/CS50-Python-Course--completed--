emptlist = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
numlist = ["1","2","3","4","5","6","7","8","9","10","11","12"]


while True:
    input1 = input("input please: ")
    try:
        month, day, year = input1.split("/")
        if month not in numlist:
            continue
    except ValueError:
        try:
            month, day, year = input1.split()
            if month not in emptlist:
                continue
            if "," not in day:
                continue
        except ValueError:
            print("incorrect syntax brothaaaaa")
            continue
    if "," in day:
        day = day[0:len(day)-1]
    day = int(day)
    count = 1
    for i in range(0,12):
        if month == emptlist[i] or month == numlist[i]:
            count -= 1
            break
    if day > 31 or day < 0:
        continue
    if count > 0:
        continue
    else:
        break

if month in emptlist:
    for i in range(0,len(emptlist)):
        if month == emptlist[i]:
            month = numlist[i]
            break
        else:
            continue

if int(month) < 10:
    print(f"{year}-0{month}-{day:02}")
else:
     print(f"{year}-{month}-{day:02}")



