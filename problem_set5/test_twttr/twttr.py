def main():
    klm=input("Input: ")
    print(shorten(klm))


def shorten(word):
    string = ""
    for i in word:
        if i in ["a","o","i","e","u","A","E","I","O","U"]:
            continue
        else:
            string = string + i
    return string

if __name__ == "__main__":
    main()