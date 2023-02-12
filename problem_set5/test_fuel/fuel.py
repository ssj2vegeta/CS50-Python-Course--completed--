def main():
    input1 = input("input fraction")
    print(gauge(convert(input1)))

def convert(fraction):
    try:
        first, second = fraction.split("/")
    except ValueError:
        raise ValueError
    try:
        first = int(first)
    except ValueError:
        raise ValueError
    try:
        second = int(second)
    except ValueError:
        raise ValueError
    if second == 0:
        raise ZeroDivisionError
    if first > second:
        raise ValueError
    percentage = (first/second) * 100
    return percentage


def gauge(percentage):
    if percentage >= 99 and percentage <= 100:
        return "F"

    elif percentage <= 1 and percentage >= 0:
        return "E"

    else:
        return f"{round(percentage)}%"




if __name__ == "__main__":
    main()