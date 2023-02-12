import random
while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass
        continue
    if level < 1 or level > 100:
        print("INVALID!!! - only numbers from 1 to 100 are accepted")
        continue
    else:
        break

randomnum = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
        continue
    if guess > randomnum:
        print("Too large!")
        continue
    elif guess < randomnum:
        print("Too small!")
        continue
    elif guess < 0:
        continue
    elif guess == randomnum:
        print("Just Right!")
        break

