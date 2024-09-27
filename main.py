def fib(n):
    a, b = 0, 1
    fib_seq = [a, b]

    while len(fib_seq) < n:
        next = a + b
        fib_seq.append(next)
        a, b = b, next

    return fib_seq


print(fib(10))