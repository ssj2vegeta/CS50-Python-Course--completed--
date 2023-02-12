def main():
    userinput = input("What time is it?")
    length1 = convert(userinput)
    if length1 <= 8 and length1 >= 7:
        print("breakfast time")
    elif length1 <= 13 and length1 >= 12:
        print("lunch time")
    elif length1 <= 19 and length1 >= 18:
        print('dinner time')
def convert(time):
    hours, minutes = time.split(":")
    new_minute = float(minutes) / 60
    return float(hours) + new_minute


if __name__ == "__main__":
    main()