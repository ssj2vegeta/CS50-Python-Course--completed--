from validator_collection import validators, checkers, errors
def main():
    print(validator(input("Input your email please")))

def validator(s):
    try:
        validatemail = validators.email(s)
        return "Valid"
    except (ValueError):
        return "Invalid"
    except EmptyValueError:
        return "Invalid"




if __name__ == "__main__":
    main()
