def fahrenheit_to_celsius(f):
    c = (f - 32) * (5/9)
    return c

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = n * factorial(n -1)
        return  result
