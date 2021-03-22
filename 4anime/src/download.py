import os

DOWNLOAD_DIR = "./Downloads/"


def down():
    with open('./Downloads/q.txt', 'r') as f:
        k = f.readlines()
    for i in k:
        i = i.strip('\n')
        name = i.split('/')
        print(f"Downloading Episode Number ::\t {name[-1]}")
        os.makedirs(DOWNLOAD_DIR + name[-2], exist_ok=True)
        path = DOWNLOAD_DIR + name[-2] + '/'
        # os.system(f'curl {i} -o { path + name[-1] }.mp4')
        size = os.popen(f'curl -sI {i}').read()
        if '404' in size:
            print("Not Found")
        else:
            os.system(f'curl {i} -o { path + name[-1] }.mp4')




down()
