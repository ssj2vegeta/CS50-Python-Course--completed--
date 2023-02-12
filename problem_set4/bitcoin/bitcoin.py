import sys
import requests
import json
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
o = response.json()
k = o["bpi"]
j = k['USD']
rate = j["rate_float"]
if len(sys.argv) == 2:
    try:
        float(sys.argv[1])
    except ValueError:
        raise Exception("no")
else:
    raise Exception("no")
value = float(rate) * float(sys.argv[1])
value = round(value,4)
numbers = "{:,}".format(value)
print("$" + numbers)