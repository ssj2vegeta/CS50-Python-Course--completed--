from pyfiglet import Figlet
figlet = Figlet()
import random
import sys
if len(sys.argv) == 1:
    k = random.choice(figlet.getFonts())
    figlet.setFont(font =k)
    input1 = input("Input: ")
    print(figlet.renderText(input1))
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
       if sys.argv[2] in figlet.getFonts():
         figlet.setFont(font=sys.argv[2])
         input1 = input("Input: ")
         print(figlet.renderText(input1))
       else:
         raise Exception("error")
         sys.exit()
    elif sys.argv[1] != "-f" or sys.argv[1] != "--font":
        raise Exception("error")
        sys.exit()
else:
    raise Exception("error")
    sys.exit()
figlet = Figlet()
