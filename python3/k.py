def calc(counter, number):
    if counter * 2 < number - counter:
        return calc(1 + counter, number)
    else:
        return counter


partial = 1 + 2 * calc(0, 10)
result = calc(0, partial)
print(result)
