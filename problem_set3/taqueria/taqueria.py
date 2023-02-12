menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
list1 = []
while True:
    try:
        choice = input("what would you like?")
        choice = choice.title()
    except EOFError:
        break
    try:
        menu[choice]
    except KeyError:
        print()
        pass
        continue
    list1.append(menu[choice])
    print(f"${sum(list1):.2f}")