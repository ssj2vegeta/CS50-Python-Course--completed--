import sys
from PIL import ImageOps
from PIL import Image
masterlist = []
if len(sys.argv) < 3:
    raise Exception("invalid")
count = 0
if len(sys.argv) == 3:
    if count > 1:
        raise Exception("invalid")
    else:
        try:
            image = Image.open(sys.argv[1])
            shirt = Image.open("shirt.png")
            size = shirt.size
            muppet = ImageOps.fit(image, size)
            muppet.paste(shirt, shirt)
            muppet.save(sys.argv[2])
        except FileNotFoundError:
           raise Exception("invalid")
if len(sys.argv) > 3:
    raise Exception("invalid")