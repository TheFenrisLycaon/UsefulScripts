n = int(eval(input("enter input value:")))

lst = []
m = 1

for i in range(n, 0, -1):
    lst.append(i)
    m = m * i

print(lst)
print(("factorial of", n, "is", m))