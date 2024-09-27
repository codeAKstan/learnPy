def even_numbers(n):
    a = 1
    while a < n:
        if a % 2 == 0:
            yield a
        a += 1


for i in even_numbers(10):
    print(i)