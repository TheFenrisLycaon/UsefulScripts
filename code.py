k = int(input())
num = list(map(int, input().split()))
num2 = []
for i in range(k):
    num2.append(num[i])
    # print(numset)
    res = max(set(num2), key = num2.count)
    # res = (max([k for k,v in num2.items() if v == res]))
    # print(res)
      