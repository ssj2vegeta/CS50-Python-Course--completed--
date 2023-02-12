listfruits = ['apple', 'avocado','kiwifruit','pear','sweet cherries']
fruits = {'apple': 130,
          "avocado":50,
          "kiwifruit":90,
          "pear":100,
          "sweet cherries":100}
input2 = input("Item: ")
input2 = input2.strip().lower()
if input2 in listfruits:
    print(fruits[input2])
elif input2 not in listfruits:
    print("")