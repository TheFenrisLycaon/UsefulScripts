import random
import os

music_dir = "D:\\Media\\Audio\\Collection xZ\\Darshan"
songs = os.listdir(music_dir)
for i in range(int(eval(input("Number of songs::"))) + 1):
    y = random.randint(1, 102)
    os.startfile(os.path.join(music_dir, songs[y]))
