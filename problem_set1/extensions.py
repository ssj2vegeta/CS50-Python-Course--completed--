input = input('file name please')

input = input.strip().lower()
if ".gif" in input:
    print("image/gif" )
elif ".png" in input:
    print("image/png")
elif ".pdf" in input:
    print("application/pdf")
elif ".txt" in input:
    print("text/plain")
elif ".zip" in input:
    print("application/zip")
elif ".jpg"  in input:
    print("image/jpeg")
elif ".jpeg" in input:
    print("image/jpeg")
else:
    print("application/octet-stream")