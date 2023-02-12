
value = 0
change = 0
while value < 50:
    input1 = int(input("enter:"))
    if input1 == 25 or input1 == 10 or input1 == 5:
        value += input1
        print(f"Amount due: {50 - value}")
    else:
        print(f"Amount due: {50 - value}")
        continue
change = value - 50
if value >= 50:
    print(f"Change owed: {change}")