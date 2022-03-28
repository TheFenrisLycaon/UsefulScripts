import time

print("Press ENTER to begin, Press Ctrl + C to stop")

while True:
    try:
        input()
        starttime = time.time()
        print("Started")
        while True:
            print("Time Elapsed: ", round(time.time() - starttime, 0), "secs", end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped")
        endtime = time.time()
        print("Total Time:", round(endtime - starttime, 2), "secs")
        break
