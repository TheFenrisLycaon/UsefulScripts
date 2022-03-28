import time
import os

birthdayFile = "/home/fenris/Apps/Scripts/Birthday/reminder.data"
myFilePath = "python /home/fenris/Apps/Scripts/Birthday/reminder.py"


def checkStartupScript():
    """This function ensures that our application executes on every startup"""
    flag = 0
    fileName = open("/etc/rc.local", "r")
    for line in fileName:
        if myFilePath in line:
            flag = 1
    if flag == 0:
        addToStartup()
    fileName.close()


def addToStartup():
    fileName = open("/etc/rc.local", "a")
    fileName.write(myFilePath + "\n")
    fileName.close()


def checkTodaysBirthdays():
    fileName = open(birthdayFile, "r")
    today = time.strftime("%m%d")
    flag = 0
    for line in fileName:
        if today in line:
            line = line.split(" ")
            flag = 1
            os.system('notify-send "Birthdays Today: ' + line[1] + " " + line[2] + '"')
    if flag == 0:
        os.system('notify-send "No Birthdays Today!"')


if __name__ == "__main__":
    checkStartupScript()
    checkTodaysBirthdays()
