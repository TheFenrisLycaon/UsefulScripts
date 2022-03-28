#!/usr/local/bin/python3

"""
Write a function that writes some text to a file, and then decorate it with behavior that checks beforehand whether the process has write access to the file.
"""

import os
import sys

# this function read a path from user and checks the permission
def check_path(append_to_file):
    path = eval(input(
        "Please input a path: \n+++ If a path of an existing file is given,\n+++ this program will check the permission and try to append some text to that file.\n+++ Otherwise, it will throw you corresponding errors.\n"
    ))
    # check if it's a absolute path
    if not path.startswith("/"):
        path = os.path.join(os.getcwd(), path)
    # check if it's a file
    if os.path.isfile(path):
        # check if user can write to this file
        if not os.access(path, os.W_OK):
            sys.exit("ERROR: you have no permission to write to " + path)
        else:

            def inner():
                nonlocal path
                return append_to_file(path)

            return inner
    else:
        sys.exit("ERROR: " + path + " is not an existing file!")


@check_path
def append_to_file(path):
    newline = eval(input("Please input some words: "))
    with open(path, "a") as f:
        f.write(newline + "\n")
        print("Success!")


append_to_file()
