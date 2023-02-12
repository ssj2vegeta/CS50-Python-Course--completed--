def main():
    text = convert(input("Write a message with an emoticon: "))
    print(text)


def convert(text):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")
    return text


main()