message = input("input your message")

splitmessage = message.split()
finalmessage = ""
for i in range(0,len(splitmessage)):
    finalmessage = finalmessage + i
    if i < len(splitmessage):
        finalmessage = finalmessage + "..."


