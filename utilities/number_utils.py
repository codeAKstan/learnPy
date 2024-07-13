# factorial

def fact(number):
    if number < 0:
        print("number can't be negative")
    elif number == 0 or number == 1:
        return 1
    else:
        result = number * fact(number - 1)
        return result

