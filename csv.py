import os
import re

path = 'D:/Media/Video/Book 1 - Water/'
titles = './Daily_Scripts/title.txt'
lis = []

with open(titles, 'r') as fileIn:
    lis = fileIn.read().split('\n')
    fileIn.close()

final = []
newlis = []

for _ in range(len(lis)):
    newlis.append(re.sub('["]', '', lis[_]))  
for _ in range(len(lis)):
    final.append(re.sub('[:]', ' -', newlis[_]))  

for i in final:
    if i == '':
        final.remove(i)

# for _ in final : print(_)

# print(len(final))

files = os.listdir(path)
print(len(files))

for i in range(len(files)):
    k = files[i]
    j = str(i+21) + ' - ' + final[i] + '.mkv'
    os.rename(path+k, path+j)