n = int(eval(input()))
for i in range(0, n + 1):
    print((
        (" " * (n - i) + "*" + " " * (2 * i - 1) + "*" * (i != 0)) * (i != n)
        + ("*" * (n * 2 + 1)) * (i == n)
    ))
