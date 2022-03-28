while True:

    a = eval(input())
    b = eval(input())

    y = str(eval(input()))

    if "add" in y:
        print((a + b))

    elif "sub" in y:
        print((a - b))

    elif "cross" in y:
        print((a * b))

    elif "divide" in y:
        print((a / b))

    else:
        print("Not Defined")
