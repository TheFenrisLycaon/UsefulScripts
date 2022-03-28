import time

from selenium import webdriver

count = int(eval(input("Number of times to be repeated: ")))
url = eval(input("Enter the URL : "))
print("Length of video:")
minutes = int(eval(input("Minutes ")))
seconds = int(eval(input("Seconds ")))

refreshrate = minutes * 60 + seconds

driver = webdriver.Chrome()

if url.startswith("https://"):
    driver.get(url)
else:
    driver.get("https://" + url)

for i in range(count):
    time.sleep(refreshrate)
    driver.refresh()
