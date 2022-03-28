import time

print(
    'Press "ENTER" to begin\nAfterwards, press "ENTER" to "click" the stopwatch.\nPress Ctrl-C to quit.'
)
input()
print("Started.")

startTime = time.time()
lastTime = startTime
lapNum = 1
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print("Lap #%s: %s (%s)" % (lapNum, totalTime, lapTime), end="")
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print("\nDone.")
