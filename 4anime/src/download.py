from pathlib import Path
import os
import sys

DOWNLOAD_DIR = str(Path.home()) + "/Downloads/Anime/"


def down(filename):
    global links
    with open(filename, 'r') as f:
        links = f.readlines()
    for link in links:
        j = link
        link = link.strip('\n')
        name = link.split('/')
        os.makedirs(DOWNLOAD_DIR + name[-2], exist_ok=True)
        path = DOWNLOAD_DIR + name[-2] + '/'
        os.system(f'wget {link} -cP {path}')
        links.remove(j)

def update(links):
    with open(DOWNLOAD_DIR+"q.txt", 'w') as f:
        f.writelines(links)
    f.close()


try:
    if len(sys.argv) > 1:
        fName = sys.argv[-1]
    else:
        fName = input("Enter download list path::\t")
    down(fName)
except Exception as e:
    # print("No files to download.")
    print(e)

update(links)