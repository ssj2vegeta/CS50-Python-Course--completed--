import sys
from pyfiglet import Figlet
figlet = Figlet()
if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
       if sys.argv[2] in figlet.getFonts():
         figlet.setFont(font=sys.argv[2])
         input1 = input("Input: ")
         print(figlet.renderText(input1))
       else:
         print("Invalid Usage")
         sys.exit()
    elif sys.argv[1] != "-f" or sys.argv[1] != "--font":
        print("Invalid Usage")
        sys.exit()