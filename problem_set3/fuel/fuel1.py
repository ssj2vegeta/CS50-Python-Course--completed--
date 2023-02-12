while True:
    fraction = (input("input yo fraction"))
    try:
        first, second = fraction.split("/")
    except ValueError:
        pass
    try:
        first = int(first)
    except (NameError, ValueError) as error:
        pass
        continue
    try:
        second = int(second)
    except (NameError, ValueError) as error:
        pass
        continue
    try:
        result = round(100 * (first/second))
    except ZeroDivisionError:
        pass
        continue
    if result > 100:
        continue
    elif result >= 99 and result <= 100:
        print("F")
        break
    elif result <= 1 and result >= 0:
        print("E")
        break
    else:
        print(f"{round(result)}%")
        break