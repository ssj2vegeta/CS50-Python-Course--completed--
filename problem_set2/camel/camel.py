input1 = input("camelCase:")
empt = ""
for c in input1:
    if c.isupper() == True:
        empt = empt + "_"
    empt  = empt + c
print(empt.lower())