message = input("input your message")

splitmessage = message.split()
finalmessage = ""
for i in range(0,len(splitmessage)):
    finalmessage = finalmessage + splitmessage[i]
    if i < len(splitmessage) -1:
        finalmessage = finalmessage + "..."

print(finalmessage)