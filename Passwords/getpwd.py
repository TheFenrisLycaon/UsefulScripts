import os
import re
import string
import sys
import termios
import time
import tty

PROMPT = "Enter Password : "
MASK = "*"


def check_strength(password: str) -> bool:
    password = "".join(map(chr, password))
    return True if (re.fullmatch(r"^[A-Za-z0-9@#$%^&+=]{8,32}$", password)) else False


def getwch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def display_msg(PROMPT: str, delay: int = 0) -> None:
    for ch in PROMPT:
        print(ch, end="", flush=True)
        if delay is not None:
            time.sleep(delay)


def getpw(minlength=8, maxlength=32, delay=None, strong=True) -> str:
    display_msg(PROMPT)

    length = range(minlength, maxlength)
    length_err = "\nlength is too {}, please enter a value in range of {}!"

    password = []

    while True:
        ch = ord(getwch())
        if ch == 13:
            if len(password) not in length:
                s1 = "short" if len(password) < length[0] else "long"
                s2 = f"({length[0]} - {length[-1] + 1})"
                print(length_err.format(s1, s2))
                return getpw()
            elif strong:
                if check_strength(password):
                    print("\nPassword is too weak")
                    return getpw()
            break

        elif ch == 127:
            if len(password) != 0:
                sys.stdout.write("\b \b")
                sys.stdout.flush()
            password = password[:-1]
            continue

        elif ch == 2:
            sys.stdout.write("\b \b" * len(password))
            sys.stdout.flush()
            password = []
            continue

        elif ch == 3:
            raise KeyboardInterrupt

        if chr(ch) in string.printable:
            password.append(ch)
            print(MASK, end="", flush=True)

    print(flush=True)

    return "".join(map(chr, password))
