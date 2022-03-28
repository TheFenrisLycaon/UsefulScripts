#!/usr/local/bin/python3

"""
Calculate the time elapsed between consecutive events in the Apache access log.
"""

from datetime import datetime
import re

# this function yields a datetime object from each line in the log
def create_datetime():
    for each_line in open("/etc/httpd/logs/access_log", "r"):

        # print the raw record, so users can see the original time
        print(("*" * 20, "NEXT EVENT", "*" * 20, "\n", each_line))

        # use RE to filter all date, time info from each line
        # then create a datetime object from them
        yield datetime.strptime(
            re.findall("\[(.*?)\]", each_line)[0], "%d/%b/%Y:%H:%M:%S %z"
        )


event = create_datetime()

# create the first datetime object
first_event = next(event)

while True:
    try:
        # create the second datetime object
        second_event = next(event)
        print(("Time elapsed since last event:", str(second_event - first_event), "\n"))
        # keep the second datetime object, so I can use it again
        first_event = second_event
        quit = eval(input("Press enter to continue, any other key to quit:\n"))
        if quit:
            break
    except StopIteration:
        break
