list1 = []
list2 = []
while True:
    try:
        grocerylist = input("")
    except EOFError:
        break
    list1.append(grocerylist.upper())
    list2.append(grocerylist.upper())
list1.sort()
for i in list1:
    count = 0
    for j in list2:
        if j == i:
            count += 1
    while True:
        try:
            list2.remove(i)
        except ValueError:
            break
    if count > 0:
        print(f"{count} {i}")
    else:
        continue