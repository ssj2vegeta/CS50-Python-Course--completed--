import inflect
p = inflect.engine()
basestring = "Adieu, adieu, to "
namelist = []
while True:
    try:
        name = input("Name: ")
        namelist.append(name)
    except EOFError:
        break
print()
mylist = p.join(namelist)
print(basestring + mylist)