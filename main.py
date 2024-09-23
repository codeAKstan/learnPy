def countdown(num):
    print("counting down")

    while num > 0:
        yield num
        num -= 1

for i in countdown(7):
    print(i)