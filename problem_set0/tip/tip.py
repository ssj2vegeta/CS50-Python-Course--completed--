
def dollars_to_float(dollar):
    dollarss = float(dollar[1:6])
    dollarsss = round(dollarss, 1)
    return dollarsss

def percent_to_float(percentss):
    percents = float(percentss[:-1])
    percentss = percents / 100
    return percentss




def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")




main()