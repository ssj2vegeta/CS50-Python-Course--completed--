input1 = input("what expression would you like to perform?")

def calculator():
    if input1[2] == "+":
        value1 = int(input1[0])+int(input1[4])
        return float(value1)
    elif input1[2] == "-":
        value2 = int(input1[0]) - int(input1[4])

        return float(value2)
    if input1[2] == "*":
        value3 =  int(input1[0]) * int(input1[4])
        return float(value3)
    if input1[2] == "/":
        value4 = int(input1[0]) / int(input1[4])
        return float(value4)
    else:
        return 10.0
print(calculator())