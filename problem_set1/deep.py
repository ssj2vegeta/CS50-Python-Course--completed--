userinput = input("What is the answer to the Great Question of Life, the Universe, and Everything?")

userinput = userinput.strip().lower()
match userinput:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
