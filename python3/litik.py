x = 1
while x:
    n = int(input())
    if n != None:
        for i in range(0, n - 1):
            for j in range(0, i + 1):
                if j != n:
                    if j == 0 or j == i:
                        print("*", end="")
                    else:
                        print(" ", end="")
            print()
        print("*" * n)
    else:
        x -= 1
