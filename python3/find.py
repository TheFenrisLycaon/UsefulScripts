#!/usr/local/bin/python3

"""
Write a function that, given a directory, yields all the files it contains, recursively. Make sure to catch PermissionError and distinguish between relative and absolute paths.

"""

import os


def check_path(path):
    # check if it's a absolute path
    if not path.startswith("/"):
        path = os.path.join(os.getcwd(), path)
    # check if this path exists
    if not os.path.exists(path):
        print((path + " <<< ERROR: this path doesn't exisit!"))
    # symbolic links may cause infinite loop, so I'm not going to trace them
    if os.path.islink(path):
        print((path + " <<< This is a symbolic link."))
        return
    try:
        # the recusive part
        # loop through everything under the path
        for folder in os.listdir(path):
            # the "yield from" expression allows a generator to delegate
            # part of its operations to another generator.
            # for more details, please read:
            # http://legacy.python.org/dev/peps/pep-0380/
            # check_path(os.path.join(path,folder)) is a subgenerator
            # it calls the further subgenerator and return the value
            # to the outer generator. So it works recursively
            yield from check_path(os.path.join(path, folder))
    except OSError:
        # if it's a file, just print it out
        if os.path.isfile(path):
            print(path)
        # check if the user has permission to read this folder
        elif not os.access(path, os.R_OK):
            print((path + " <<< ERROR: you don't have permission to read this folder!"))


path = eval(input("Please input a path: "))
folder = check_path(path)
while True:
    try:
        next(folder)
    except StopIteration:
        break
